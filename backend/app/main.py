from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import chat
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(title="Critical Thinking AI Backend")

# Enable CORS for local dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, use a specific domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(chat.router)

@app.get("/")
def root():
    return {"message": "AI Middleware Backend is running"}
