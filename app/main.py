import os
from fastapi import FastAPI
from app.controllers.user_controller import router as user_router
from app.controllers.data_controller import router as data_router
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# Include routers
app.include_router(user_router, prefix="/api/users")
app.include_router(data_router, prefix="/api/data")

# Ensure the correct absolute path for static files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

# Serve static files
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/")
async def serve_welcome():
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8001"))  # Default to 8001 if not set
    uvicorn.run(app, host="0.0.0.0", port=port, reload=True)