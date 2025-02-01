from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all domains
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

marks_file = "marks.json"
if os.path.exists(marks_file):
    with open(marks_file, "r") as f:
        student_marks = json.load(f)
else:
    student_marks = {}

@app.get("/api")
def get_marks(name: list[str] = []):
    """Fetch marks for given student names"""
    if not name:
        return {"error": "No names provided"}
    
    marks = [student_marks.get(n, None) for n in name]
    return {"marks": marks}
