from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router.Studentrouter import router as Student_router

app = FastAPI(title="Ecommerce API")

# Allow Flask app to talk to FastAPI without CORS issues
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Attach router endpoints to main app
app.include_router(Student_router)



