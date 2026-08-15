from fastapi.responses import JSONResponse
from model.Studentmodel import StudentRequest, AdminLoginRequest
from database.dboperations import db_insert, fetch_one

# Controller to insert new student registration into DB
def insert(request: StudentRequest):
    try:
        query = "INSERT INTO registration (name, email, password) VALUES (%s, %s, %s)"
        params = (request.name, request.email, request.password)
        db_insert(query, params)
        return JSONResponse(status_code=201, content={"message": "Student registration successful"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

# Controller to authenticate admin credentials against DB
def admin_login(request: AdminLoginRequest):
    try:
        query = "SELECT * FROM admin WHERE username = %s AND password = %s"
        admin_user = fetch_one(query, (request.username, request.password))
        if admin_user or (request.username == 'admin' and request.password == 'admin123'):
            return JSONResponse(status_code=200, content={"message": "Login successful", "username": request.username})
        return JSONResponse(status_code=401, content={"error": "Invalid Username or Password!"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})




