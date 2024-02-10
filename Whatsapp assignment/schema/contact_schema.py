from pydantic import BaseModel, Field,  StrictStr, model_validator
from typing import Optional
# from user_schema import UserSchema
class ContactSchema(BaseModel):
    '''Schema for the User api by which fastapi uses to interact with database'''
    id: str = Field(..., min_length=3, max_length=50)
    name:str = Field(... , min_length=1, max_length=50)
    phone_no:str = Field(...,min_length=10, max_length=10)
    image:str
    # user:
   
    