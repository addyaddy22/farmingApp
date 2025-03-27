from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.models import FarmData
from app.views.schemas import FarmDataCreate, FarmOptionsDataCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
#Data submit route
@router.post("/submit")
def submit_data(data: FarmDataCreate, db: Session = Depends(get_db)):
    db_data = FarmData(**data.dict())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data


@router.post("/submitoptions")
def FarmDataOptions(data: FarmOptionsDataCreate, db: Session = Depends(get_db)):
    db_data = FarmData(**data.dict())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data