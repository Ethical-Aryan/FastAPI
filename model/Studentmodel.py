from pydantic import BaseModel
from typing import List, Optional

# Connects: router/Studentrouter.py & controller/Studentcontroller.py
class StudentRequest(BaseModel):
    name: str
    gender: str
    mobile: str
    email: str

# Connects: controller/Studentcontroller.py
class StudentResponse(BaseModel):
    id: int
    name: str
    mobile: str
    email: str
    address: str
    enroll_id: str
    subjects: List[str]



