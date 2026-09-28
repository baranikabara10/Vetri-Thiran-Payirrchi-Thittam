import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations


# Load .env
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent


# Create FastAPI application
app = FastAPI(
    title="EduGenie",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0"
)


# Static files
app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)


# HTML templates
templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)


# -----------------------------
# Request Models
# -----------------------------

class TextRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=30000
    )


# -----------------------------
# Home Page
# -----------------------------

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "title": "EduGenie"
        }
    )


# -----------------------------
# Health Check
# -----------------------------

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "gemini_configured": bool(
            os.getenv("GEMINI_API_KEY")
        )
    }


# -----------------------------
# Q&A API
# -----------------------------

@app.post("/qa")
async def qa(data: TextRequest):

    result = answer_question(data.text)

    return {
        "result": result
    }


# -----------------------------
# Explanation API
# -----------------------------

@app.post("/explain")
async def explain(data: TextRequest):

    result = explain_topic(data.text)

    return {
        "result": result
    }


# -----------------------------
# Quiz API
# -----------------------------

@app.post("/quiz")
async def quiz(data: TextRequest):

    result = generate_quiz(data.text)

    return {
        "result": result
    }


# -----------------------------
# Summary API
# -----------------------------

@app.post("/summarize")
async def summarize(data: TextRequest):

    result = summarize_text(data.text)

    return {
        "result": result
    }


# -----------------------------
# Learning Path API
# -----------------------------

@app.post("/learn/recommendations")
async def recommendations(data: TextRequest):

    result = get_learning_recommendations(data.text)

    return {
        "result": result
    }