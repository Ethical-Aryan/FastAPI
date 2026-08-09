from fastapi import FastAPI 
from fastapi.responses import JSONResponse

obj = FastAPI()

#Single Query parameter
@obj.get("/single")
def single(name):
    message = "Welcome " + name
    return JSONResponse(status_code=200,content={"data":message })

#Multi Query Parameter ,fixing datatype and giving default value
@obj.get("/multiple") 
def multiple(id:int,name:str,mobile:int,email:str,address=""):
    try:
        message = "Welcome " + str(id) + name + str(mobile) + email + address   
        return JSONResponse(status_code=200,content={"data":message })
    except Exception as e:
         return JSONResponse(status_code=500,content={"data":str(e) })  

@obj.get("/home")
def home():
    return JSONResponse(content={"data":"Welcome to JSON"})