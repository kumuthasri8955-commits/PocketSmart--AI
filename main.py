from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from gemini_utils import ask_gemini

app = FastAPI()


class UserRequest(BaseModel):
    prompt: str

@app.get("/login")
def login_page():
    return FileResponse("templates/login.html")

@app.get("/")
def home():
    return FileResponse("templates/index.html")

@app.post("/generate")
def generate(request: UserRequest):
    result = ask_gemini(request.prompt)
    return {"recommendation": result}

@app.post("/generate-home")
def generate_home(request: UserRequest):
    prompt = "You are a home interior planning assistant. " + request.prompt
    result = ask_gemini(prompt)
    return {"recommendation": result}


@app.post("/generate-party")
def generate_party(request: UserRequest):
    prompt = "You are a party planning assistant. " + request.prompt
    result = ask_gemini(prompt)
    return {"recommendation": result}


@app.post("/generate-jewelry")
def generate_jewelry(request: UserRequest):
    prompt = "You are a jewelry recommendation assistant. " + request.prompt
    result = ask_gemini(prompt)
    return {"recommendation": result}