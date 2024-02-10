from pydantic import BaseModel, Field,  StrictStr, model_validator
from typing import Optional, List
from schema.contact_schema import ContactSchema

class MessageSchema(BaseModel):
    '''Schema for the User api by which fastapi uses to interact with database'''
    id: str = Field(..., min_length=3, max_length=50)
    # type:str = Field(..., min_length=3, max_length=50)
    recieverId:str = Field(..., min_length=3, max_length=50)
    content:str 
    
    # @model_validator(mode="after")
    # def validate_imageurl(self):
    #     '''Mark:- Imageurl
    #     Imageurl cannot be null or empty
    #     '''
    #     image_url = self.image
    #     if image_url is None:
    #         raise ValueError("Image url cannot be null")
    #     if not image_url.strip():
    #         raise ValueError("Image url cannot be empty")
        
        # return self

class TextSchema(MessageSchema):
    content :str 
 
class AudioSchema(MessageSchema):
    content :str 

class VideoSchema(MessageSchema):
    content :str 

