from app.database import engine, Base
from app.models.models import User, FarmData,FarmDataOptions

# Create all tables
Base.metadata.create_all(bind=engine)