import json
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Load once on startup
with open("courses.json", "r") as f:
    courses = json.load(f)

@app.get("/")
async def root():
    return {"message": "Hello, Railway!"}

@app.get("/courses/{category}")
async def get_course(category: str):
    # category will be URL-decoded automatically
    data = courses
    if data is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return data

# new /leader route
@app.get("/leader")
async def get_leader():
    return {"name": "shereen"}

