from pydantic import BaseModel

class Item(BaseModel):
    id:int
    heading: str
    description:str


