# resumes/views.py
from django.http import JsonResponse
from rest_framework.views import APIView
from .resume_parser import parse_resume
from .models import Candidate
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class ResumeUploadView(APIView):
    def post(self, request):
        file = request.FILES.get('file')
        if file:
            resume_text = file.read().decode('utf-8')
            name, email, skills, experience = parse_resume(resume_text)
            candidate = Candidate.objects.create(
                name=name, 
                email=email,
                skills=", ".join(skills),
                years_of_experience=experience
            )
            return JsonResponse({'id': candidate.id})

        return JsonResponse({'error': 'No file uploaded'}, status=400)


class JobMatchView(APIView):
    def post(self, request, candidate_id):
        try:
            candidate = Candidate.objects.get(id=candidate_id)
        except Candidate.DoesNotExist:
            return JsonResponse({'error': 'Candidate not found'}, status=404)
        
        # Example job descriptions (simplified)
        jobs = [
            {"title": "Data Scientist", "skills": ["python", "machine learning", "data analysis"]},
            {"title": "Web Developer", "skills": ["python", "django", "html", "css", "javascript"]},
            {"title": "Software Engineer", "skills": ["java", "c++", "data structures"]}
        ]

        candidate_skills = candidate.skills.split(", ")
        job_titles = []
        similarity_scores = []

        # Compare candidate skills to job descriptions using cosine similarity
        for job in jobs:
            job_skills = job["skills"]
            all_skills = list(set(candidate_skills + job_skills))
            candidate_vector = np.array([1 if skill in candidate_skills else 0 for skill in all_skills])
            job_vector = np.array([1 if skill in job_skills else 0 for skill in all_skills])
            similarity = cosine_similarity([candidate_vector], [job_vector])[0][0]
            job_titles.append(job["title"])
            similarity_scores.append(similarity)

        # Return best match
        best_match_index = np.argmax(similarity_scores)
        return JsonResponse({
            "job_match": job_titles[best_match_index],
            "scores": similarity_scores
        })
