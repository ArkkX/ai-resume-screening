from flask import request, jsonify
from werkzeug.utils import secure_filename
from utils import extract_text_from_pdf, extract_text_from_docx, preprocess_text, extract_entities
import os

def initialize_routes(app):
    @app.route('/upload-resume', methods=['POST'])
    def upload_resume():
        if 'file' not in request.files:
            return jsonify({"error": "No file provided"}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        if filename.endswith('.pdf'):
            text = extract_text_from_pdf(file_path)
        elif filename.endswith('.docx'):
            text = extract_text_from_docx(file_path)
        else:
            return jsonify({"error": "Unsupported file format"}), 400

        entities = extract_entities(preprocess_text(text))
        return jsonify({"filename": filename, "entities": entities}), 200

    @app.route('/submit-job-description', methods=['POST'])
    def submit_job_description():
        data = request.json
        if not data or 'description' not in data:
            return jsonify({"error": "Job description not provided"}), 400
        description = preprocess_text(data['description'])
        entities = extract_entities(description)
        return jsonify({"description": description, "entities": entities}), 200

    @app.route('/match-resume', methods=['POST'])
    def match_resume():
        data = request.json
        if not data or 'resume_entities' not in data or 'job_entities' not in data:
            return jsonify({"error": "Resume or Job entities missing"}), 400

        resume_entities = data['resume_entities']
        job_entities = data['job_entities']

        scores = {
            "skills": len(set(resume_entities["skills"]) & set(job_entities["skills"])),
            "education": len(set(resume_entities["education"]) & set(job_entities["education"])),
            "experience": len(set(resume_entities["experience"]) & set(job_entities["experience"]))
        }
        weights = {"skills": 0.5, "education": 0.3, "experience": 0.2}
        total_score = sum(scores[category] * weights[category] for category in scores)
        return jsonify({"scores": scores, "total_score": total_score}), 200
