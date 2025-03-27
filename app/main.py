import os
from fastapi import FastAPI
from app.controllers.user_controller import router as user_router
from app.controllers.data_controller import router as data_router

app = FastAPI()

# Include routers
app.include_router(user_router, prefix="/api/users")
app.include_router(data_router, prefix="/api/data")

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8001"))  # Default to 8001 if not set
    uvicorn.run(app, host="0.0.0.0", port=port, reload=True)