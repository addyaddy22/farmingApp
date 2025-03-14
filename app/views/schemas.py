from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    firstname: str
    password: str
    email: str
    role: str

class UserLogin(BaseModel):
    username: str
    password: str

class FarmDataCreate(BaseModel):
    farmer_name: str
    nation_id: str
    farm_type: str
    crop: str
    location: str

class FarmOptionsDataCreate(BaseModel):
    farm_type: str
    crop: str
    location: str