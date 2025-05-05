# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import network
from app.database import init_db
app = FastAPI(title="Innovaxel Assessment test Name : Muhammad Haroon Siddique")


 
# 🔥 Allow CORS for Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # ✅ Allow frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # ✅ Allow all HTTP methods (GET, POST, DELETE, etc.)
    allow_headers=["*"],  # ✅ Allow all headers
)
# Include routers
app.include_router(network.router, prefix="/network", tags=["APis"])


# Root endpoint
@app.get("/")
async def root():
    return {"message": "welcome to url shortener"}
