from fastapi import FastAPI 
from fastapi.responses import JSONResponse
from pydantic import BaseModel , Field
from typing import List

obj = FastAPI(title="Aryan's Ecommerce API  ")

class StudentRequest(BaseModel):
    id:int
    name:str
    mobile:int
    email:str
    address:str
    

class StudentResponse(BaseModel):
    id:int
    name:str
    mobile:int
    email:str
    address:str
    enroll_id:str
    subjects:List[str]
    
class LoginRequests(BaseModel):
    user:str
    password:str

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

@obj.get("/getlogin") #LOGIN API
def getlogin(user:str,password:str):
    try:
        if user == "admin" and password =="admin123":
            return JSONResponse(status_code=200,content={"message":"Login Successful"})
        else:
            return JSONResponse(status_code=401, content={"message": "Login unsuccessful"} )
    except Exception as e:
             return JSONResponse(status_code=500,content={"Error message: " : str(e)})

@obj.post("/postlogin") #LOGIN POST API
def postlogin(login:LoginRequests):
    try:
        if login.user == "admin" and login.password =="admin123":
            return JSONResponse(status_code=200,content={"message":"Login Successful"})
        else:
            return JSONResponse(status_code=401, content={"message": "Login unsuccessful"} )
    except Exception as e:
             return JSONResponse(status_code=500,content={"Error message: " : str(e)})

@obj.post("/insert")
def insert(response:StudentResponse):
    try:
        response = StudentResponse(
            id = response.id,
            name = response.name,
            mobile = response.mobile,
            email = response.email, 
            address = response.address,
            enroll_id = response.enroll_id,
            subjects = response.subjects
        )
        return JSONResponse(status_code=201,content={"response":response.model_dump()})
    except Exception as e:
        return JSONResponse(status_code=500,content={"response":str(e)})

@obj.delete("/delete")
def delete(id:int):
    try:
        response = f"Deleted data of id {str(id)}"
        return JSONResponse(status_code=200,content={"response":response})
    except Exception as e:
        return JSONResponse(status_code=500,content={"response":str(e)})

@obj.get("/home")
def home():
    return JSONResponse(content={"data":"Welcome to JSON"})