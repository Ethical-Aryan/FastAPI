from fastapi.responses import JSONResponse
# Connects: model/Studentmodel.py
from model.Studentmodel import StudentRequest, StudentResponse

# Step 4: Business logic for insert
def insert(request: StudentRequest):
    try:
        # Build response payload
        response = StudentResponse(
            name=request.name,
            gender=request.gender,
            mobile=str(request.mobile),
            email=request.email, 
        )
        return JSONResponse(status_code=201, content={"response": response.model_dump()})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


