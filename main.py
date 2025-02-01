from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS (Allow all origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin
    allow_methods=["GET"],  # Only allow GET requests
    allow_headers=["*"],
)

# Load student marks from a file
with open("marks.json", "r") as f:
    student_marks = json.load(f)

@app.get("/api")
def get_marks(name: list[str] = []):
    """Fetch marks for given student names"""
    marks = [student_marks.get(n, None) for n in name]
    return {"marks": marks}
