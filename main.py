from fastapi import FastAPI 
from fastapi.responses import JSONResponse
from pydantic import BaseModel  

obj = FastAPI()

class StudentRequest(BaseModel):
    id:int
    name:str
    mobile:int
    email:str
    address:str

# class LoginRequests(BaseModel):
#     email:str
#     password:str

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

#single parameter 
@obj.get("/single-param/{name}/details")
def single_param(name):
    message = "Welcome " + name
    return JSONResponse(status_code=200,content={"data":message })

#multiple parameter
@obj.get("/multiple-param/{id}/{name}") 
def multiple_param(id:int,name:str):
    try:    
        message = "Welcome " + str(id) + " "+ name  
        return JSONResponse(status_code=200,content={"data":message })
    except Exception as e:
         return JSONResponse(status_code=500,content={"data":str(e) })  

@obj.post("/details")
def details(details:StudentRequest):
    try:
         return JSONResponse(status_code=200,content={"message":details.model_dump()})
    except Exception as e:
        return JSONResponse(status_code=500,content={"Error message: " : str(e)})

@obj.get("/login") #LOGIN API
def login(user:str,password:str):
    try:
        if user == "admin" and password =="admin123":
            return JSONResponse(status_code=200,content={"message":"Login Successful"})
        else:
            return JSONResponse(status_code=401, content={"message": "Login unsuccessful"} )
    except Exception as e:
             return JSONResponse(status_code=500,content={"Error message: " : str(e)})

@obj.get("/home")
def home():
    return JSONResponse(content={"data":"Welcome to JSON"})