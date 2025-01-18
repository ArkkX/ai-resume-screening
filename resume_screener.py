from resume_parser import ResumeParser
from keyword_matcher import KeywordMatcher
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def main():
    # Job description and required skills
    job_description = """
    We are looking for a software engineer with strong skills in Python, Machine Learning,
    and SQL. Knowledge of Data Analysis and Project Management is a plus.
    """
    skill_keywords = ["Python", "Machine Learning", "SQL", "Data Analysis", "Project Management"]

    resume_file = "-" # Change this to the resume folder/file path

    # Step 1: Parse the resume
    print("Parsing resume...")
    parser = ResumeParser(resume_file)
    parsed_resume = parser.parse_resume(skill_keywords)
    print("Resume Parsed Successfully!")

    # Step 2: Match resume with job description
    print("\nMatching skills with job requirements...")
    matcher = KeywordMatcher(job_description, skill_keywords)
    match_result = matcher.match_keywords(parsed_resume)

    # Step 3: Display results
    print("\n===== Candidate Fit Analysis =====")
    print("Contact Info:", parsed_resume["contact_info"])
    print("Education:", parsed_resume["education"])
    print("Work Experience:", parsed_resume["work_experience"])
    print("Certifications:", parsed_resume["certifications"])
    print("Projects:", parsed_resume["projects"])
    print("\nSkill Analysis:")
    print("Matching Skills:", match_result["matching_skills"])
    print("Missing Skills:", match_result["missing_skills"])
    print("Match Score:", match_result["match_score"], "%")

def generate_report(candidate_data, filename="report.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    c.drawString(100, 750, "Candidate Screening Report")
    y = 700

    for candidate in candidate_data:
        c.drawString(100, y, f"Name: {candidate['contact_info']['name']}")
        c.drawString(100, y-20, f"Match Score: {candidate['match_score']}%")
        c.drawString(100, y-40, f"Matching Skills: {', '.join(candidate['matching_skills'])}")
        c.drawString(100, y-60, f"Missing Skills: {', '.join(candidate['missing_skills'])}")
        y -= 100

    c.save()


if __name__ == "__main__":
    main()
