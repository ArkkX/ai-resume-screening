from resume_parser import ResumeParser
from keyword_matcher import KeywordMatcher

class CandidateRanker:
    def __init__(self, resumes, job_description, skill_keywords):
        self.resumes = resumes
        self.job_description = job_description
        self.skill_keywords = skill_keywords
        self.results = []

    def rank_candidates(self):
        for resume_file in self.resumes:
            parser = ResumeParser(resume_file)
            parsed_resume = parser.parse_resume(self.skill_keywords)

            matcher = KeywordMatcher(self.job_description, self.skill_keywords)
            match_result = matcher.match_keywords(parsed_resume)

            self.results.append({
                "file": resume_file,
                "contact_info": parsed_resume.get("contact_info"),
                "match_score": match_result.get("match_score"),
                "matching_skills": match_result.get("matching_skills"),
                "missing_skills": match_result.get("missing_skills"),
            })

        # Sort candidates by match score in descending order
        self.results.sort(key=lambda x: x["match_score"], reverse=True)
        return self.results


# Example Usage
if __name__ == "__main__":
    # Job description and skill keywords
    job_description = """
    We are looking for a software engineer with strong skills in Python, Machine Learning,
    and SQL. Knowledge of Data Analysis and Project Management is a plus.
    """
    skill_keywords = ["Python", "Machine Learning", "SQL", "Data Analysis", "Project Management"]

    # List of resumes to compare
    resumes = ["candidate1.pdf", "candidate2.pdf", "candidate3.pdf"]

    ranker = CandidateRanker(resumes, job_description, skill_keywords)
    ranked_candidates = ranker.rank_candidates()

    print("\n===== Ranked Candidates =====")
    for i, candidate in enumerate(ranked_candidates, start=1):
        print(f"{i}. {candidate['contact_info']['name']} - Match Score: {candidate['match_score']}%")
        print(f"   Matching Skills: {candidate['matching_skills']}")
        print(f"   Missing Skills: {candidate['missing_skills']}\n")
