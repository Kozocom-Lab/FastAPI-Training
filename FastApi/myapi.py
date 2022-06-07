# from fastapi import FastAPI, Path, Query, HTTPException, status
# from typing import Optional
# from typing import Union
# from pydantic import BaseModel

# app = FastAPI()

# students = {
#     1: {
#         "name": "join",
#         "age": 17,
#         "year": "Year 12"
#     }
# }

# class Student(BaseModel):
#     name: str
#     age: int
#     year: str

# class UpdateStudent(BaseModel):
#     name: Optional[str] = None
#     age: Optional[int] = None
#     year: Optional[str] = None


# @app.get("/")
# def index():
#     return {"name": "First Data"}

# @app.get("/get_student/{studentId}")
# def get_student(studentId: int = Path(None, description="The ID not found", gt = 0, lt =3)):
#     return students[studentId]

# @app.get("/get-by-name")
# async def get_student(name = Query(None, title="Name", description="Name of item")):
#     for student_id in students:
#         if students[student_id]["name"] == name:
#             return students[student_id]
#     raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail ="Students not found")

# @app.post("/create-students/{student_id}")
# def create_student(student_id: int, student: Student):
#     if student_id in students:
#         return {"Data": "Students Exist"}
    
#     students[student_id] = student
#     return students[student_id]

# @app.put("/update-student/{studentId}")
# def update_student(student_id, student: UpdateStudent):
#     if student_id not in students:
#         return {"Data": "Not found"}
#     students[student_id] = student
#     return students

# @app.delete("/delete-student")
# def delete_student(student_id: int = Query(..., description="The ")):
#     if student_id in students:
#         del students[student_id]
#         return {"Succeess": "ssss"}

# @app.get("/students/{user_id}/items/{item_id}")
# async def read_user_item(
#     user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
# ):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item

# # @app.get("/items/")
# # async def read_items(q: str = Query(default="fixedquery", min_length=3)):
# #     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
# #     if q:
# #         results.update({"q": q})
# #     return results
# # @app.get("/items/")
# # async def read_items(
# #     q: Union[str, None] = Query(
# #         default=None,
# #         alias="item-query",
# #         title="Query string",
# #         description="Query string for the items to search in the database that have a good match",
# #         min_length=3,
# #         max_length=50,
# #         regex="^fixedquery$",
# #         deprecated=True,
# #     )
# # ):
# #     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
# #     if q:
# #         results.update({"q": q})
# #     return results


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None



# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item
#     # if item.tax:
#     #     price_with_tax = item.price + item.tax
#     #     item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict
import re

# define list of places
listOfPlaces = ["Bayswater", "Table Bay", "Bejing", "Bombay"]

# define search string
pattern = re.compile("[Bb]ay")

for place in listOfPlaces:  
    if pattern.search(place):
        print ("%s matches the search pattern" % place)