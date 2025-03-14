from fastapi import FastAPI
from app.controllers.user_controller import router as user_router
from app.controllers.data_controller import router as data_router

app = FastAPI()

# Include routers
app.include_router(user_router, prefix="/api/users")
app.include_router(data_router, prefix="/api/data")