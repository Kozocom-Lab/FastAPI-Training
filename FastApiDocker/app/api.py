from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from requests import session
from sqlalchemy.orm import Session
from crud import get_all, create_car, create_user, update_car_info, get_model_info_by_id, delete_model_info, update_user_info
from database import get_db
from exceptions import ModelInfoException
from schemas import Car, User, CreateAndUpdateCar, CreateAndUpdateUser, PaginatedCarInfo
from models import CarInfo, UserInfo

router = APIRouter()

@cbv(router)
class Cars:
    session: Session = Depends(get_db)
   
    # API to get the list of car info
    @router.get("/cars")
    def list_cars(self, limit: int = 10, offset: int = 0):
        cars_list = get_all(self.session, CarInfo, limit, offset)
        response = {"limit": limit, "offset": offset, "data": cars_list}

        return response
    
    @router.post("/cars")
    def add_car(self, car_info: CreateAndUpdateCar):
        try:
            car_info = create_car(self.session, car_info)
            return car_info
        except ModelInfoException as cie:
            raise HTTPException(**cie.__dict__)

@cbv(router)
class Users:
    session: Session = Depends(get_db)
    @router.get("/users")
    def list_users(self, limit: int = 10, offset: int = 0):
        users_list = get_all(self.session, UserInfo, limit, offset)
        response = {"limit": limit, "offset": offset, "data": users_list}

        return response
    
    @router.post("/users")
    def add_car(self, user_info: CreateAndUpdateUser):
        try:
            user_info = create_user(self.session, user_info)
            return user_info
        except ModelInfoException as cie:
            raise HTTPException(**cie.__dict__)


@router.get("/cars/{car_id}", response_model=Car)
def get_car_info(car_id: int, session: Session = Depends(get_db)):
    try:
        car_info = get_model_info_by_id(session,CarInfo, car_id)
        return car_info
    except ModelInfoException as cie:
        raise HTTPException(**cie.__dict__)


# API to update a existing car info
@router.put("/cars/{car_id}", response_model=Car)
def update_car(car_id: int, new_info: CreateAndUpdateCar, session: Session = Depends(get_db)):
    try:
        car_info = update_car_info(session, car_id, new_info)
        return car_info
    except ModelInfoException as cie:
        raise HTTPException(**cie.__dict__)


# API to delete a car info from the data base
@router.delete("/cars/{car_id}")
def delete_car(car_id: int, session: Session = Depends(get_db)):
    try:
        return delete_model_info(session,CarInfo, car_id)
    except ModelInfoException as cie:
        raise HTTPException(**cie.__dict__)

@router.get("/users/{user_id}", response_model=User)
def get_user_info(user_id: int, session: Session = Depends(get_db)):
    try:
        car_info = get_model_info_by_id(session,UserInfo, user_id)
        return car_info
    except ModelInfoException as cie:
        raise HTTPException(**cie.__dict__)


# API to update a existing car info
@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, new_info: CreateAndUpdateCar, session: Session = Depends(get_db)):
    try:
        car_info = update_user_info(session, user_id, new_info)
        return car_info
    except ModelInfoException as cie:
        raise HTTPException(**cie.__dict__)


# API to delete a car info from the data base
@router.delete("/users/{user_id}")
def delete_user(user_id: int, session: Session = Depends(get_db)):
    try:
        return delete_model_info(session,UserInfo, user_id)
    except ModelInfoException as cie:
        raise HTTPException(**cie.__dict__)