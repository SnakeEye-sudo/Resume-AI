from sqlalchemy import Column, Integer, String, ForeignKey, Text, Float, JSON, DateTime, ARRAY
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.session import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    resumes = relationship("Resume", back_populates="owner")

class Resume(Base):
    __tablename__ = "resumes"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    filename = Column(String)
    parsed_data = Column(JSON)  # Stores extracted entities
    text_content = Column(Text) # Raw text
    ats_score = Column(Integer)
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())
    
    owner = relationship("User", back_populates="resumes")
    matches = relationship("ResumeJobMatch", back_populates="resume")

class JobPosting(Base):
    __tablename__ = "job_postings"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    company = Column(String, index=True)
    description = Column(Text)
    required_skills = Column(ARRAY(String))
    experience_years = Column(Integer)
    scraped_at = Column(DateTime(timezone=True), server_default=func.now())
    
    matches = relationship("ResumeJobMatch", back_populates="job")

class ResumeJobMatch(Base):
    __tablename__ = "resume_job_matches"
    id = Column(Integer, primary_key=True, index=True)
    resume_id = Column(Integer, ForeignKey("resumes.id"))
    job_id = Column(Integer, ForeignKey("job_postings.id"))
    match_score = Column(Float)
    skill_match_percentage = Column(Float)
    gaps = Column(JSON)  # Missing skills, experience gap
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    resume = relationship("Resume", back_populates="matches")
    job = relationship("JobPosting", back_populates="matches")
