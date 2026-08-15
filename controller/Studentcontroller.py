from fastapi.responses import JSONResponse
# Connects: model/Studentmodel.py
from model.Studentmodel import StudentRequest, StudentResponse
from database.dbconnection import insert
# Step 4: Business logic for insert
def createrequest(request:createrequest):
    try:
        query = f"Insert into registration (name,email,PASSWORD ) values('{request.name}','{request.email}','{request.PASSWORD}')"
        insert_response = insert(query)
        # Build response payload

        return JSONResponse(status_code=201, content={"response": response.model_dump()})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


