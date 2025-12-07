from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Resume AI Backend", version="1.0.0")

# CORS Setup
origins = [
    "http://localhost:3000",
    "http://localhost:5173",  # Vite default
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from app.api.endpoints import resume
import uvicorn

app.include_router(resume.router, prefix="/api/v1", tags=["resume"])

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
