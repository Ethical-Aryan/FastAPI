from fastapi import FastAPI 
from fastapi.responses import JSONResponse

obj = FastAPI()

@obj.get("/display")
def display():
    return {"Welcome to first API"}

@obj.get("/home")
def home():
    return JSONResponse(content={"data":"Welcome to JSON"})