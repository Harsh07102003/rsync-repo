from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# --- Response Models ---
# Define response models for better validation and API documentation.
class Message(BaseModel):
    message: str

class HealthStatus(BaseModel):
    status: str

# Add metadata for your application for better documentation.
app = FastAPI(
    title="Demo FastAPI App",
    description="A demonstration of a scalable FastAPI application structure.",
    version="0.1.0",
)

# Add CORS middleware to allow cross-origin requests, crucial for web frontends.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for demo purposes. For production, restrict this.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_model=Message)
async def read_root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Hello FastAPI!"}

@app.get("/health", response_model=HealthStatus)
async def health_check():
    """
    Health check endpoint to verify the service is running.
    """
    return {"status": "ok"}
