from typing import Any, List, Optional
from sqlalchemy.orm import Session
from exceptions import ModelInfoAlreadyExistError, ModelInfoNotFoundError
from models import CarInfo, UserInfo
from schemas import CreateAndUpdateCar, CreateAndUpdateUser
from database import Base
import logging

def get_all(session: Session, model: Base, limit: int, offset: int) -> List[Base]:
    return session.query(model).offset(offset).limit(limit).all()

def get_model_info_by_id(session: Session, model: Base, _id: int) -> Base:
    model_info = session.query(model).get(_id)
    if model_info is None:
        raise ModelInfoNotFoundError(str(model))
    
    return model_info

def create_car(session: Session, car_info: CreateAndUpdateCar) -> CarInfo:
    car_details = session.query(CarInfo).filter(CarInfo.manufacturer == car_info.manufacturer, CarInfo.modelName == car_info.modelName).first()
    if car_details is not None:
        raise ModelInfoAlreadyExistError("Car")

    new_car_info = CarInfo(**car_info.dict())
    session.add(new_car_info)
    session.commit()
    session.refresh(new_car_info)

    return new_car_info


# Function to update details of the car
def update_car_info(session: Session, _id: int, info_update: CreateAndUpdateCar) -> CarInfo:
    car_info = get_model_info_by_id(session, CarInfo, _id)

    if car_info is None:
        raise ModelInfoNotFoundError("Car")

    car_info.manufacturer = info_update.manufacturer
    car_info.modelName = info_update.modelName
    car_info.fuelType = info_update.fuelType
    car_info.cc = info_update.cc
    car_info.gearBox = info_update.gearBox
    car_info.onRoadPrice = info_update.onRoadPrice
    car_info.seatingCapacity = info_update.seatingCapacity

    session.commit()
    session.refresh(car_info)

    return car_info


# Function to delete a car info from the db
def delete_model_info(session: Session, model: Base, _id: int):
    model_info = get_model_info_by_id(session, model, _id)

    if model_info is None:
        raise ModelInfoNotFoundError(str(model))

    session.delete(model_info)
    session.commit()

    return

def create_user(session: Session, user_info: CreateAndUpdateUser) -> UserInfo:
    logging.info(user_info.dict())
    new_user_info = UserInfo(**user_info.dict())
    session.add(new_user_info)
    session.commit()
    session.refresh(new_user_info)

    return new_user_info

def update_user_info(session: Session, _id: int, info_update: CreateAndUpdateUser) -> UserInfo:
    user_info = get_model_info_by_id(session, UserInfo, _id)
    if user_info is None:
        raise ModelInfoNotFoundError("User")

    user_info.name = info_update.name
    user_info.email = info_update.email
    user_info.gender = info_update.gender

    session.commit()
    session.refresh(user_info)

    return user_info
