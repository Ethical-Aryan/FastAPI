from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router.Studentrouter import router as Student_router
from database.dboperations import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize database tables and starter seed data on startup
    try:
        init_db()
        print("[OK] Database tables initialized successfully.")
    except Exception as e:
        print(f"[ERROR] Database initialization failed: {e}")
    yield

app = FastAPI(title="Ecommerce API", lifespan=lifespan)

# Allow Flask app to talk to FastAPI without CORS issues
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root health check endpoint
@app.get("/")
def root():
    return {"status": "online", "message": "FastAPI Ecommerce Backend is running", "docs": "/docs"}

# Attach router endpoints to main app
app.include_router(Student_router)
