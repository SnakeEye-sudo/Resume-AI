# Resume-AI Complete Setup Guide

## ⚡ Quick Setup (5 minutes)

### Windows Users - One Command Setup:
```cmd
# Copy and paste this in Command Prompt
git clone https://github.com/SnakeEye-sudo/Resume-AI.git && cd Resume-AI && python -m venv venv && venv\Scripts\activate && pip install -r backend/requirements.txt && python -m spacy download en_core_web_trf && start cmd /k "cd backend && uvicorn app.main:app --reload" && cd frontend && npm install && npm run dev
```

### Linux/Mac Users - One Command Setup:
```bash
# Copy and paste this in Terminal
git clone https://github.com/SnakeEye-sudo/Resume-AI.git && cd Resume-AI && python -m venv venv && source venv/bin/activate && pip install -r backend/requirements.txt && python -m spacy download en_core_web_trf && (cd backend && uvicorn app.main:app --reload &) && cd frontend && npm install && npm run dev
```

---

## 📋 Prerequisites Check

Before starting, make sure you have:

```bash
# Check Python version (needs 3.12+)
python --version

# Check Node.js version (needs 18+)
node --version

# Check npm version
npm --version

# Check if Ollama is installed
ollama --version
```

**If any are missing:**
- [Python 3.12+](https://www.python.org/downloads/)
- [Node.js 18+](https://nodejs.org/)
- [Ollama](https://ollama.com/) - Download and install
- [PostgreSQL](https://www.postgresql.org/download/) (optional for full features)

---

## 🚀 Step-by-Step Setup

### Step 1: Clone Repository
```bash
git clone https://github.com/SnakeEye-sudo/Resume-AI.git
cd Resume-AI
```

### Step 2: Backend Setup (Terminal 1)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r backend/requirements.txt

# Download NLP model
python -m spacy download en_core_web_trf

# Start Ollama (if not already running)
# Open another terminal and run:
ollama pull llama3.2

# Run backend server
cd backend
uvicorn app.main:app --reload
```

**Backend Running at:** `http://localhost:8000`

### Step 3: Frontend Setup (Terminal 2)
```bash
# In new terminal, from project root
cd frontend
npm install
npm run dev
```

**Frontend Running at:** `http://localhost:5173`

---

## ✅ Verification Checklist

Once everything is running:

- [ ] Backend terminal shows: `Uvicorn running on http://127.0.0.1:8000`
- [ ] Frontend terminal shows: `Local: http://localhost:5173`
- [ ] Open browser and visit: `http://localhost:5173`
- [ ] UI loads without errors
- [ ] Upload a test resume (PDF or DOCX)
- [ ] Paste a test job description
- [ ] Click "Analyze" and wait for results

---

## 🆘 Troubleshooting

### Backend Won't Start
```bash
# Try updating pip
python -m pip install --upgrade pip

# Clear cache and reinstall
pip cache purge
pip install -r backend/requirements.txt --force-reinstall
```

### Node modules issues
```bash
# Delete node_modules and reinstall
rm -rf frontend/node_modules package-lock.json
npm install
```

### Ollama not running
```bash
# On Windows:
# Make sure Ollama is installed and running in the background

# On Linux/Mac:
ollama serve
# In another terminal:
ollama pull llama3.2
```

### Port already in use
```bash
# Kill process on port 8000 (backend)
# Windows:
netstat -ano | findstr :8000

# Change port in backend/app/main:
uvicorn app.main:app --reload --port 8001
```

---

## 🌐 Deploy to GitHub Pages

### Build Frontend
```bash
cd frontend
npm run build
```

### Upload to GitHub Pages
1. Go to Repository Settings → Pages
2. Select branch: `main`
3. Select folder: `/frontend/dist`
4. Save

**Live Demo Link:** `https://snakeeye-sudo.github.io/Resume-AI/`

---

## 📱 API Endpoints

Once backend is running, test endpoints:

```bash
# Health check
curl http://localhost:8000/health

# Parse Resume
POST http://localhost:8000/api/parse-resume
Body: { "resume_path": "path/to/resume.pdf" }

# Match Job
POST http://localhost:8000/api/match-job
Body: { "resume_text": "...", "job_description": "..." }

# Get AI Suggestions
POST http://localhost:8000/api/suggestions
Body: { "resume_text": "...", "job_description": "..." }
```

---

## 🎯 What to Test

1. **Resume Upload**: PDF and DOCX formats
2. **Job Description**: Paste any job description
3. **Matching**: Check if compatibility score appears
4. **3D Visualization**: Rotate the skill graph
5. **AI Suggestions**: Wait for Ollama response
6. **No Data Leak**: Check network tab - no API calls

---

## 📊 Tech Stack Verification

- **Backend**: FastAPI ✅
- **Frontend**: React 18 ✅
- **NLP**: SpaCy ✅
- **AI**: Ollama/Llama 3.2 ✅
- **Database**: SQLAlchemy ORM ✅
- **3D Graphics**: Three.js ✅

---

## 🚀 Next Steps

- [ ] Star the repo ⭐
- [ ] Try the live demo
- [ ] Share feedback in Issues
- [ ] Submit PRs for improvements
- [ ] Fork and customize for your needs

---

## 💬 Questions?

Check the main [README.md](./README.md) for more details or open an issue on GitHub.

**Happy Resume Matching! 🎉**
