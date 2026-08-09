from fastapi import FastAPI

obj = FastAPI()

@obj.get("/display")
def display():
    return {"Welcome to first API"}