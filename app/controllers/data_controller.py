from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.models import FarmData
from app.views.schemas import FarmDataCreate, FarmOptionsDataCreate, FarmDataResponse
from typing import List
from sqlalchemy import func, distinct  # <-- Add this import



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
    print("received data", data.dict())
    db_data = FarmDataOptions(**data.dict())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

# Get all farmers data route
@router.get("/farmers", response_model=list[FarmDataResponse])
def get_all_farmers(db: Session = Depends(get_db)):
    farmers = db.query(FarmData).all()
    return farmers



@router.get("/farmers/stats")
def get_farmer_stats(db: Session = Depends(get_db)):
    # Total number of farmers
    total_farmers = db.query(func.count(FarmData.id)).scalar()
    
    # Total number of unique crops
    total_crops = db.query(func.count(distinct(FarmData.crop))).scalar()
    
    # Count locations 
    total_locations = db.query(func.count(distinct(FarmData.location))).scalar()

    return {
        "total_farmers": total_farmers,
        "total_crops": total_crops,
        "total_locations": total_locations
    }