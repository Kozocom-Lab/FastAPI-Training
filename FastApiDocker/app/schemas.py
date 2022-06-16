from pydantic import BaseModel
from models import Gender, FuelType
from typing import Optional, List

class CreateAndUpdateCar(BaseModel):
    manufacturer: str
    modelName: str
    cc: int
    onRoadPrice: int
    seatingCapacity: int
    gearBox: int
    fuelType: FuelType

class Car(CreateAndUpdateCar):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class CreateAndUpdateUser(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    gender: Optional[Gender] = None

class User(CreateAndUpdateUser):
    id: Optional[int] = None

# To support list cars API
class PaginatedCarInfo(BaseModel):
    limit: int
    offset: int
    data: List[Car]
