# Resume AI - Local AI-Powered Resume Analyzer & Job Matcher 🚀

> **⭐ If you find this project helpful, please star it! It helps other developers discover this tool.**

![GitHub Stars](https://img.shields.io/github/stars/SnakeEye-sudo/Resume-AI?style=social)
![GitHub Forks](https://img.shields.io/github/forks/SnakeEye-sudo/Resume-AI?style=social)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.12+-blue)
![React](https://img.shields.io/badge/React-18+-blue)

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

## 📱 Try Live Demo (GitHub Pages)

Want to try the app without setting up locally? You can access the live demo here:
- **Live Demo**: [Resume-AI Demo](https://snakeeye-sudo.github.io/Resume-AI/)
- **Note**: For full functionality, the backend server must be running locally. This demo connects to your local backend.

### Steps to use the live demo:
1. Clone the repository and run the backend server (see Backend Setup above)
2. Visit the [Live Demo Link](https://snakeeye-sudo.github.io/Resume-AI/)
3. Upload your resume and job description
4. The frontend will communicate with your local backend API

## 🤝 Contributing

Issues and Pull Requests are welcome!

## 🌟 Why Resume AI?

- **Privacy First**: Your resume data NEVER leaves your computer
- **No API Costs**: Run everything offline with local LLMs
- **Job Search Ready**: Perfect for optimizing resumes for ATS systems
- **Developer Friendly**: Built with React + FastAPI for easy customization
- **100% Open Source**: MIT licensed, contributions welcome!

## 📊 Use Cases

- 🎯 Job Seekers: Analyze your resume against multiple job descriptions
- 📝 Career Changers: Identify skill gaps and get AI-powered suggestions
- 🤖 Researchers: Study NLP/ML techniques in resume parsing
- 💼 HR Professionals: Understand ATS scoring for better hiring

## 🏆 Key Differentiators

| Feature | Resume AI | Other Tools |
|---------|-----------|-------------|
| Privacy | 100% Local | Cloud-based |
| Cost | Free (Open Source) | Paid/Freemium |
| AI Suggestions | Local LLM (Llama) | GPT API |
| Customizable | Full source available | Limited |
| Data Security | Complete | Third-party dependent |

## 📞 Support & Community

- 📖 [Full Documentation](https://github.com/SnakeEye-sudo/Resume-AI/wiki)
- 🐛 [Report Issues](https://github.com/SnakeEye-sudo/Resume-AI/issues)
- 💡 [Feature Requests](https://github.com/SnakeEye-sudo/Resume-AI/discussions)
- ⭐ **Star this repo if you find it useful!**

---

<div align="center">

### Show your support - ⭐ Star this repository!

Every star helps us reach more job seekers and developers.

[![Star on GitHub](https://img.shields.io/github/stars/SnakeEye-sudo/Resume-AI?style=social)](https://github.com/SnakeEye-sudo/Resume-AI)

</div>
