from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.dialects.postgresql import ENUM
from app.database import Base

#  ENUM type for user roles
user_roles = ENUM("clerk", "admin", name="user_roles", create_type=False)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    firstname = Column(String)
    password = Column(String)
    email = Column(String)
    role = Column(user_roles)

class FarmData(Base):
    __tablename__ = "farm_data"
    id = Column(Integer, primary_key=True, index=True)
    farmer_name = Column(String)
    nation_id = Column(String)
    farm_type = Column(String)
    crop = Column(String)
    location = Column(String)

class FarmDataOptions(Base):
    __tablename__ = "farm_data_options"
    id = Column(Integer, primary_key=True, index=True)
    farm_type = Column(String)
    crop = Column(String)
    location = Column(String)


