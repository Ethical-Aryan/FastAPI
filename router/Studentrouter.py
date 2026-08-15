from fastapi import APIRouter 
from controller.Studentcontroller import insert, admin_login
from model.Studentmodel import StudentRequest, AdminLoginRequest

router = APIRouter()

@router.post("/student/insert")
def student_insert(request: StudentRequest):
    return insert(request)

@router.post("/admin/login")
def admin_login_route(request: AdminLoginRequest):
    return admin_login(request)



