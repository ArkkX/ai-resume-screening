# AI Resume Screener

AI Resume Screener is a full-stack prototype that automates the initial screening of candidate resumes against arbitrary job descriptions. It extracts and classifies resume content, computes transparent sub-scores (Education, Experience, Projects, Skills), and ranks candidates by overall fit. The system is built with:

- **Backend**: Python 3.10, FastAPI, Uvicorn  
- **Parsing**: pdfplumber, pdf2image + pytesseract (OCR), PyPDF2, python-docx  
- **Section Classification**: spaCy TextCategorizer (custom model)  
- **Scoring**: regex- and heuristic-based sub-scores + Sentence-Transformers embeddings  
- **Frontend**: Next.js, React, Axios

## Table of Contents

1. [Features](#features)  
2. [Prerequisites](#prerequisites)  
3. [Installation](#installation)  
4. [Configuration](#configuration)  
5. [Running the Application](#running-the-application)  
   - [Backend](#backend)  
   - [Frontend](#frontend)  
6. [Usage](#usage)  
7. [Project Structure](#project-structure)  
8. [Testing](#testing)  
9. [Contribution](#contribution)  
10. [License](#license)  
11. [Contact](#contact)

## Features

- **Multi-format ingestion**: PDF, DOCX, LinkedIn/GitHub URLs  
- **Robust parsing pipeline**: layout → OCR → text-fallback  
- **Section classification**: Education, Experience, Projects, Skills, Summary, Other  
- **Hybrid scoring engine**: transparent heuristics + semantic skill matching  
- **Bulk upload & ranking**: upload many resumes at once, get a sorted shortlist  
- **Interactive UI**: paste job description, select files, view detailed breakdowns  

## Prerequisites

- **Python 3.10**  
- **Node.js 18.x** & **npm**  
- **Poppler** (for `pdf2image`)  
- **Tesseract OCR** (for `pytesseract`)  
- Git (to clone repo)

## Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/ai-resume-screener.git
   cd ai-resume-screener
   ```

2. **Backend setup**  
   ```bash
   cd backend
   python3.10 -m venv .venv
   source .venv/bin/activate   # macOS/Linux
   # .venv\Scripts\Activate.ps1 # Windows PowerShell
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```

3. **Frontend setup**  
   ```bash
   cd ../frontend
   npm install
   ```

## Configuration

- **Backend**  
  - Copy `.env.example` to `.env` and adjust if needed (e.g. model directory).  
  - Requires `POPPLER_PATH` in your system PATH and Tesseract installed.

- **Frontend**  
  - Copy `.env.local.example` to `.env.local`:
    ```ini
    NEXT_PUBLIC_API_URL=http://localhost:8000
    ```

## Running the Application

### Backend

```bash
cd backend
source .venv/bin/activate    # or activate in Windows
uvicorn app.main:app --reload
```

- API docs available at:  
  - Swagger UI: http://localhost:8000/docs  
  - ReDoc:       http://localhost:8000/redoc  

### Frontend

```bash
cd frontend
npm run dev
```

- Open http://localhost:3000 in your browser.

## Usage

1. Navigate to **Upload Resumes** page.  
2. Paste your **Job Description** in the text box.  
3. Click **Choose Files** and select one or more PDF/DOCX resumes.  
4. Click **Score & Rank Resumes**.  
5. View ranked results, with sub-scores and highlighted text snippets.

## Project Structure

```
ai-resume-screener/
├─ backend/
│  ├─ app/
│  │  ├─ advanced_parsing.py
│  │  ├─ parsing.py
│  │  ├─ semantic_matching.py
│  │  ├─ scoring.py
│  │  ├─ enhanced_scoring.py
│  │  ├─ train_spacy_textcat.py
│  │  ├─ main.py
│  │  └─ dependencies.py
│  ├─ .venv/
│  └─ requirements.txt
├─ frontend/
│  ├─ components/
│  │  ├─ Navbar.jsx
│  │  └─ UploadForm.jsx
│  ├─ pages/
│  │  ├─ index.js
│  │  └─ upload.js
│  ├─ public/
│  ├─ styles/
│  │  └─ globals.css
│  └─ package.json
├─ README.md
├─ docker-compose.yml
└─ LICENSE
```

## Testing

### Unit & Integration

```bash
cd backend
. .venv/bin/activate
pytest -q
```

### End-to-End (Playwright)

```bash
cd frontend
npx playwright test
```

### Load Testing (k6)

```bash
k6 run loadtest.js
```

## License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## Contact

*Your Name* • [your.email@example.com](mailto:your.email@example.com)  
Project repository: https://github.com/yourusername/ai-resume-screener  
```
