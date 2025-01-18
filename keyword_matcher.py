class KeywordMatcher:
    def __init__(self, job_description, skill_keywords):
        self.job_description = job_description.lower()
        self.skill_keywords = [skill.lower() for skill in skill_keywords]

    def match_keywords(self, parsed_resume):
        """
        Compare the parsed resume with job requirements and calculate a match score.
        """
        matching_skills = [
            skill for skill in parsed_resume.get("skills", []) if skill.lower() in self.skill_keywords
        ]

        missing_skills = [
            skill for skill in self.skill_keywords if skill not in [s.lower() for s in parsed_resume.get("skills", [])]
        ]

        match_score = len(matching_skills) / len(self.skill_keywords) * 100

        return {
            "matching_skills": matching_skills,
            "missing_skills": missing_skills,
            "match_score": round(match_score, 2),
        }


# Example Usage
if __name__ == "__main__":
    # Example job description and required skills
    job_description = """
    We are looking for a software engineer with strong skills in Python, Machine Learning,
    and SQL. Knowledge of Data Analysis and Project Management is a plus.
    """
    skill_keywords = ["Python", "Machine Learning", "SQL", "Data Analysis", "Project Management"]

    # Parsed resume data (output from ResumeParser)
    parsed_resume = {
        "skills": ["Python", "SQL", "Data Analysis", "C++"],
    }

    matcher = KeywordMatcher(job_description, skill_keywords)
    match_result = matcher.match_keywords(parsed_resume)

    print("Matching Skills:", match_result["matching_skills"])
    print("Missing Skills:", match_result["missing_skills"])
    print("Match Score:", match_result["match_score"], "%")
