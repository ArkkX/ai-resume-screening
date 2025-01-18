import re
from pdfplumber import open as pdf_open
from docx import Document


class ResumeParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.text = self._extract_text()

    def _extract_text(self):
        """Extract text from PDF or DOCX."""
        if self.file_path.endswith('.pdf'):
            return self._extract_from_pdf()
        elif self.file_path.endswith('.docx'):
            return self._extract_from_docx()
        else:
            raise ValueError("Unsupported file format. Use PDF or DOCX.")

    def _extract_from_pdf(self):
        with pdf_open(self.file_path) as pdf:
            return " ".join([page.extract_text() for page in pdf.pages])

    def _extract_from_docx(self):
        doc = Document(self.file_path)
        return " ".join([paragraph.text for paragraph in doc.paragraphs])

    def extract_contact_info(self):
        """Extract contact information: name, email, phone, LinkedIn, GitHub."""
        email = re.search(r'[\w\.-]+@[\w\.-]+', self.text)
        phone = re.search(r'\+?\d[\d -]{8,}\d', self.text)
        linkedin = re.search(r'(https?://)?(www\.)?linkedin\.com/in/[a-zA-Z0-9-]+', self.text)
        github = re.search(r'(https?://)?(www\.)?github\.com/[a-zA-Z0-9-]+', self.text)
        name_match = re.search(r'^\s*([A-Za-z][A-Za-z\s]*[A-Za-z])', self.text)  # Assuming the name is at the top.

        return {
            "name": name_match.group(0).strip() if name_match else None,
            "email": email.group(0) if email else None,
            "phone": phone.group(0) if phone else None,
            "linkedin": linkedin.group(0) if linkedin else None,
            "github": github.group(0) if github else None,
        }

    def extract_education(self):
        """Extract education details: degree, institution, year."""
        education_pattern = re.compile(r'(B\.?Sc|M\.?Sc|Ph\.?D|Bachelor|Master|Doctorate|Diploma)[^,\n]*,\s*(.*?),\s*(\d{4})')
        matches = education_pattern.findall(self.text)
        education_details = [{"degree": match[0], "institution": match[1], "year": match[2]} for match in matches]
        return education_details

    def extract_work_experience(self):
        """Extract work experience: job title, company, dates, and responsibilities."""
        experience_pattern = re.compile(r'(?P<title>.+?)\s+at\s+(?P<company>.+?),\s*(?P<dates>\d{4}-\d{4})')
        matches = experience_pattern.findall(self.text)
        work_experience = [{"title": match[0], "company": match[1], "dates": match[2]} for match in matches]
        return work_experience

    def extract_skills(self, skill_keywords):
        """Extract skills matching the provided keywords."""
        skills = [skill for skill in skill_keywords if skill.lower() in self.text.lower()]
        return list(set(skills))

    def extract_certifications(self):
        """Extract certifications."""
        cert_pattern = re.compile(r'Certified\s+(.*?)(?:,|\n)')
        matches = cert_pattern.findall(self.text)
        return matches

    def extract_projects(self):
        """Extract projects."""
        projects_pattern = re.compile(r'Project\s+Name:\s*(.*?)(?:\n|$)')
        matches = projects_pattern.findall(self.text)
        return matches

    def parse_resume(self, skill_keywords):
        """Parse the resume and return structured data."""
        return {
            "contact_info": self.extract_contact_info(),
            "education": self.extract_education(),
            "work_experience": self.extract_work_experience(),
            "skills": self.extract_skills(skill_keywords),
            "certifications": self.extract_certifications(),
            "projects": self.extract_projects(),
        }
    def anonymize_resume(self):
        """
        Remove identifiable details like name, email, phone, LinkedIn, and GitHub from the parsed resume.
        """
        anonymized_resume = self.parse_resume(skill_keywords=[])
        anonymized_resume["contact_info"] = {
            "name": "Anonymous",
            "email": "Hidden",
            "phone": "Hidden",
            "linkedin": "Hidden",
            "github": "Hidden",
        }
        return anonymized_resume



# Example Usage:
if __name__ == "__main__":
    skill_keywords = ["Python", "Java", "Machine Learning", "Data Analysis", "SQL", "Project Management"]

    # Replace 'sample_resume.pdf' with the path to your resume file
    parser = ResumeParser("C:/Users/aasri/Downloads/V.N Aasrit Durbha.pdf")
    result = parser.parse_resume(skill_keywords)
    print(result)
