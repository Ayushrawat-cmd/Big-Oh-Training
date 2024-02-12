from pydantic import BaseModel
from Models.item import Item
class User(BaseModel):
    id : int
    name: str
    age: int
    gender : str
    task: list[Item] = [] 