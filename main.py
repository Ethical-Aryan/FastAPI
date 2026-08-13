from fastapi import FastAPI
# Connects: router/Studentrouter.py
from router.Studentrouter import router as Student_router

# Step 1: Main App entrypoint
obj = FastAPI(title="Aryan's Ecommerce API")

# Step 2: Main app se router attach
obj.include_router(Student_router)

