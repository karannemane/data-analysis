from fastapi import FastAPI, UploadFile, Form
import shutil
from agent import run_agent

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Agentic CSV AI running"}

@app.post("/analyze")
async def analyze_csv(
    file: UploadFile,
    question: str = Form(...)
):
    file_path = f"data/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    answer = run_agent(f"{question} on {file_path}")
    return {"answer": answer}
