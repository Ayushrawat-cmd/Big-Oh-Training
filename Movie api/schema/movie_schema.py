from pydantic import BaseModel, Field,  StrictStr, model_validator
from typing import Optional

class MovieSchema(BaseModel):
    '''Schema for the Movie api by which fastapi uses to interact with database'''
    id: str = Field(..., min_length=3, max_length=50)
    name:str = Field(... , min_length=1, max_length=50)
    rating: Optional[int] = None
    image:StrictStr
    
    @model_validator(mode="after")
    def validate_ratings(self):
        '''Mark:- Movie ratings
        Validation for rating 
        It can be none
        '''
        rating = self.rating
        if rating < 1 or rating >10:
            raise ValueError('Rating should not be less than 1 or greater than 10')   

        return self
    
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
