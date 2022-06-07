from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException, status, Query
from typing import List, Optional
from models import Gender, Role, User, UserUpdateRequest
import re

app = FastAPI()

db: List[User] = [
    User(
        id = UUID('672cf452-cf1e-49ac-bcdd-f3be51118008'),
        first_name="Thao",
        last_name="Thao",
        gender=Gender.male,
        roles=[Role.student, Role.admin]
    ),
    User(
        id = UUID('75e85622-4ec7-446b-ba6a-d1db9bf3f723'),
        first_name="Thao1",
        last_name="Thao1",
        gender=Gender.male,
        roles=[Role.student, Role.admin]
    )
]

@app.get("/")
async def root():
    return {"Hello": "Thảo"}

@app.get("/api/v1/users")
async def fetch_users(
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    middle_name: Optional[str] = None,
    search: Optional[str] = Query(
        default=None,
        alias="key-search",
        title="Key search",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50
    )):
    users: List[User] = db
   
    if search:
        users = await search_users(search)
    else:
        if first_name is not None:
            users = await search_users(first_name, "first_name")
        if last_name is not None:
            users = await search_users(last_name, "last_name", users)
        if middle_name is not None:
            users = await search_users(middle_name, "middle_name", users)

    return users

async def search_users(keysearch: Optional[str] = None, attribute: Optional[str] = None, list_users: Optional[List[User]] = db):
    pattern = re.compile(keysearch)
    users: List[User] = []
    
    for user in list_users:
        if attribute == None and (
            pattern.search(getattr(user, 'first_name')) or 
            pattern.search(getattr(user, 'last_name')) or 
            pattern.search(getattr(user, 'middle_name'))
        ):
            users.append(user)
        elif pattern.search(getattr(user, attribute)):
            users.append(user)

    return users

@app.get("/api/v1/users/{user_id}")
async def fetch_user_detail(user_id: UUID):
    for user in db:
        if user.id == user_id:
            return user
    await responseBody(
        status.HTTP_404_NOT_FOUND,
        f"User with id: {user_id} does not exist"
    )

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    await responseBody("Register user succcess")

    return user

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            await responseBody("Delete user succcess")

            return
    await responseBody(
        status.HTTP_404_NOT_FOUND,
        f"User with id: {user_id} does not exist"
    )

@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            await responseBody("Update user succcess")

            return
    await responseBody(
        status.HTTP_404_NOT_FOUND,
        f"User with id: {user_id} does not exist"
    )

async def responseBody(
    description: Optional[str] = None,
    status: Optional[int] = status.HTTP_200_OK
):
    raise HTTPException(
        status_code=status,
        detail=description
    )

