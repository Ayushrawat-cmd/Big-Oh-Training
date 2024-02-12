from fastapi import status
from dataclasses import dataclass
from pydantic import BaseModel, Field
from fastapi.responses import ORJSONResponse

class ErrorModel(BaseModel):
    error: str = Field(..., description='The error message description')

@dataclass
class ErrorResponse():
    def __init__(self, message):
        self.error = message

@dataclass
class GenericError:
    status: int
    message: str
    error_code: str
    error: str

class Errors():
    '''Defining all the error'''
    #orjson converts the usual data to the json format
    
    HTTP_500_INTERNAL_SERVER_ERROR = ORJSONResponse(ErrorResponse('Internal Server Error'), status.HTTP_500_INTERNAL_SERVER_ERROR)
    HTTP_404_NOT_FOUND = ORJSONResponse(ErrorResponse('Content not found on DB'), status.HTTP_404_NOT_FOUND)
    HTTP_400_BAD_REQUEST = lambda message: ORJSONResponse(ErrorResponse(message), status.HTTP_400_BAD_REQUEST)

def throw_error(status, message: str, error_code: int, error: Exception):
    error_res = GenericError(status = int(status), message = message, error_code = error_code, error = str(error))
    return ORJSONResponse(error_res, status)