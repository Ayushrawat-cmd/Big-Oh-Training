from pydantic import BaseModel, Field,  StrictStr, model_validator
from typing import Optional, List
from schema.contact_schema import ContactSchema

class UserSchema(BaseModel):
    '''Schema for the User api by which fastapi uses to interact with database'''
    id: str = Field(..., min_length=3, max_length=50)
    name:str = Field(... , min_length=1, max_length=50)
    contacts: list[ContactSchema] = []
    phone_no:str = Field(...,min_length=10, max_length=10)
    image:str
   
    
    @model_validator(mode="after")
    def validate_imageurl(self):
        '''Mark:- Imageurl
        Imageurl cannot be null or empty
        '''
        image_url = self.image
        if image_url is None:
            raise ValueError("Image url cannot be null")
        if not image_url.strip():
            raise ValueError("Image url cannot be empty")
        
        return self
