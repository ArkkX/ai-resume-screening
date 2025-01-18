from flask import Flask, request, render_template
from resume_parser import ResumeParser
from keyword_matcher import KeywordMatcher

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_resume():
    if 'resume' not in request.files:
        return "No file uploaded", 400

    file = request.files['resume']
    job_description = request.form['job_description']
    skill_keywords = request.form['skill_keywords'].split(',')

    parser = ResumeParser(file)
    parsed_resume = parser.parse_resume(skill_keywords)

    matcher = KeywordMatcher(job_description, skill_keywords)
    match_result = matcher.match_keywords(parsed_resume)

    return render_template('result.html', parsed_resume=parsed_resume, match_result=match_result)

if __name__ == "__main__":
    app.run(debug=True)
