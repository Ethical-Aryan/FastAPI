from pydantic import BaseModel

# Request schema for student registration
class StudentRequest(BaseModel):
    name: str
    email: str
    password: str

# Request schema for admin login
class AdminLoginRequest(BaseModel):
    username: str
    password: str





