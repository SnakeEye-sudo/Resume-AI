# Resume AI - Local AI-Powered Resume Analyzer & Job Matcher 🚀

Privacy-focused, local-first platform that parses resumes, matches them with job descriptions, and provides AI-driven improvement suggestions using local LLMs.

## ✨ Features

- **📄 Resume Parser**: Extracts contact info, skills, experience, and education from PDF/DOCX using SpaCy & Custom Rules.
- **🎯 Job Matching Engine**: Calculates compatibility scores using TF-IDF (keywords) and Sentence Transformers (semantic meaning).
- **💡 AI Suggestions**: Privacy-preserving local AI (Ollama/Llama 3.2) analyzes gaps and suggests improvements.
- **📊 Interactive Dashboard**: 3D Skill Graphs (Three.js) and ATS Compatibility Scores.
- **🔒 100% Local**: No data leaves your machine. No API keys required.

## 🛠️ Tech Stack

### Backend
- **Framework**: FastAPI (Python 3.12)
- **NLP/ML**: SpaCy (`en_core_web_trf`), Sentence-Transformers (`all-MiniLM-L6-v2`), Scikit-learn
- **Database**: PostgreSQL (SQLAlchemy ORM)
- **AI Integration**: Ollama (Llama 3.2)

### Frontend
- **Framework**: React 18 + Vite + TypeScript
- **Styling**: Tailwind CSS
- **Visualization**: React Three Fiber (Three.js), Recharts
- **Icons**: Lucide React

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- Node.js 18+
- PostgreSQL
- [Ollama](https://ollama.com/) (running locally)

### 1. AI Model Setup
Ensure Ollama is running and pull the model:
```bash
ollama pull llama3.2
```

### 2. Backend Setup
```bash
cd backend
# Create virtual environment
python -m venv venv
# Activate (Windows)
venv\Scripts\activate
# Install dependencies
pip install -r requirements.txt
# Download NLP model
python -m spacy download en_core_web_trf
# Run Server
uvicorn app.main:app --reload
```
Server running at `http://localhost:8000`

### 3. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
Client running at `http://localhost:5173`

## 📸 Usage
1. Open the Frontend.
2. Upload your Resume (PDF/DOCX).
3. Paste a Job Description.
4. View your Match Score, Missing Skills, and AI Suggestions.

## 🤝 Contributing
Issues and Pull Requests are welcome!
