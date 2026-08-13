from fastapi import APIRouter 
# Connects: controller/Studentcontroller.py & model/Studentmodel.py
from controller.Studentcontroller import insert
from model.Studentmodel import StudentRequest

router = APIRouter()

# Step 3: POST route -> Calls controller's insert()
@router.post("/student/insert")
def student_insert(request: StudentRequest):
    return insert(request)

