from operator import index
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Enum
from database import Base
import enum

class Gender(str, enum.Enum):
    Male = "Male"
    Female = "Female"

class FuelType(str, enum.Enum):
    Petrol = "Petrol"
    Diesel = "Diesel"

class CarInfo(Base):
    __tablename__ = "car"

    id = Column(Integer, primary_key=True, index=True)
    manufacturer = Column(String)
    modelName = Column(String)
    cc = Column(Integer)
    onRoadPrice = Column(Integer)
    seatingCapacity = Column(Integer)
    gearBox = Column(Integer)
    fuelType = Column(Enum(FuelType))

class UserInfo(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    gender = Column(Enum(Gender))