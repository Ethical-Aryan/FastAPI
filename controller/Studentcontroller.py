from fastapi.responses import JSONResponse
# Connects: model/Studentmodel.py
from model.Studentmodel import StudentRequest, StudentResponse

# Step 4: Business logic for insert
def insert(request: StudentRequest):
    try:
        # Build response payload
        response = StudentResponse(
            id=request.id,
            name=request.name,
            mobile=str(request.mobile),
            email=request.email, 
            address=request.address,
            enroll_id="ENROLL_101",
            subjects=["Python", "FastAPI"]
        )
        return JSONResponse(status_code=201, content={"response": response.model_dump()})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

