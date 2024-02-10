from pathlib import Path
from fastapi_router_controller import Controller
from fastapi import Depends, HTTPException, status, Query
from fastapi.responses import JSONResponse
from typing import Annotated,Optional
from schema.errors import Errors, ErrorModel, throw_error
from environment.Router import user_router
from schema.user_schema import UserSchema
from schema.message_schema import AudioSchema
from schema.contact_schema import ContactSchema
from service.user_service import UserService
from service.contact_service import ContactService
from service.message_service import MessageService
from utils.logger import Logger
from fastapi.encoders import jsonable_encoder

controller = Controller(user_router)
logger = Logger.get_logger(__name__)

@controller.use()
@controller.resource()
class UserController:
    def __init__(self, userService:UserService = Depends(), contactService:ContactService = Depends(), messageService :MessageService = Depends()) -> None:
        # print("dsfs")
        self.userService = userService
        self.contactServie = contactService
        self.messageService = messageService

    @controller.route.get("/{id}", summary="return the user from the database", response_model=None)
    def getUserById(self, id:str= None) :
        '''Get user from the db'''
        try:
            user = self.userService.getUserById(userId=id)
            if user is None:
                return Errors.HTTP_404_NOT_FOUND
            return  JSONResponse(status_code=status.HTTP_200_OK, content={"user": jsonable_encoder(user)})
        except Exception as error:
            logger.error(f"Error in getting user {error}")
            return throw_error(status= status.HTTP_500_INTERNAL_SERVER_ERROR, message= "Internal Server Error", error_code= 500, error= error)
        

    @controller.route.get("s", summary="get all users from db", response_model=None)
    def getAllUser(self) :
        '''Get all the users from the db'''
        try:
            users = self.userService.getAllUsers()
            if users is None:
                return Errors.HTTP_404_NOT_FOUND
            return  JSONResponse(status_code=status.HTTP_200_OK, content={"users": jsonable_encoder(users)})
        except Exception as error:
            logger.error(f"Error in getting user {error}")
            return throw_error(status= status.HTTP_500_INTERNAL_SERVER_ERROR, message= "Internal Server Error", error_code= 500, error= error)

    # @controller.route.post("/{user_id}/message", response_model=None)
    # def sendMessage(self, message:AudioSchema, user_id:str =  Annotated[str, Path(title="The ID of the user to get")]):
        
    #     self.messageService.sendAudioMessage(msg=message,senderId= user_id)
    #     return  JSONResponse(status_code=status.HTTP_200_OK, content={"users": "jsonable_encoder(users)"})
    
    

    @controller.route.post("", summary="fsfds", response_model=None)
    def createUser(self, new_user: UserSchema):
        '''Create user'''
        try:
            user = self.userService.createUser(new_user)
            return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message":"User created", "user":jsonable_encoder(user)})
        except Exception as error:
            logger.error(f"Error in creating movie {error}")
            return throw_error(status= status.HTTP_500_INTERNAL_SERVER_ERROR, message= "Internal Server Error", error_code= 500, error= error)
    
    
    @controller.route.post("/{user_id}/contact", response_model=None)
    def addContact(self, new_contact: ContactSchema, user_id: Annotated[str, Path(title="The ID of the user to get")]):
        '''Add contact'''
        try:
            user = self.contactServie.addContact(new_contact=new_contact, userId=user_id)
            
            return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message":"Contact created", "user":jsonable_encoder(user)})
        except Exception as error:
            logger.error(f"Error in creating movie {error}")
            return throw_error(status= status.HTTP_500_INTERNAL_SERVER_ERROR, message= "Internal Server Error", error_code= 500, error= error)
        
    # @controller.route.put("", responses={
    #         Errors.HTTP_500_INTERNAL_SERVER_ERROR.status_code: { 
    #             'model': ErrorModel, 'description': 'Generic Error Occured' }
    #     })
    # async def updateMovie(self, movie: MovieSchema):
    #     '''Update the movie have the given details.'''
    #     try:
    #         updated_movie = self.movieService.updateMovie(movie)
    #         if updated_movie is None:
    #             return Errors.HTTP_404_NOT_FOUND
    #         # item = self.service.insertTask(newItem)
    #         return JSONResponse(status_code=status.HTTP_200_OK, content={"message":"Movie updated", "movie":jsonable_encoder(updated_movie)})
    #         # return {"message":"Task created", "task": item}
    #     except Exception as error:
    #         logger.error(f'Error insterting task: {error}')
    #         return throw_error(status= status.HTTP_500_INTERNAL_SERVER_ERROR, message= "Internal Server Error", error_code= 500 , error= error)
    
    @controller.route.delete("/{user_id}",responses={
            Errors.HTTP_404_NOT_FOUND.status_code: { 'model': ErrorModel, 'description': 'Movie not found on DB' },
            Errors.HTTP_500_INTERNAL_SERVER_ERROR.status_code: { 'model': ErrorModel, 'description': 'Generic Error Occured' }
        })
    async def deleteMovie(self,user_id: Annotated[str, Path(title="The ID of the item to get")]):
        '''Delete movie is the controller allows us delete movie from the database'''
        try:
            # print(movie_id)
            success = self.userService.deletUser(user_id)
            if success is not True:
                return Errors.HTTP_404_NOT_FOUND
            return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content={"message":"User deleted"}) 
        except Exception as error:
            logger.error(f"Error deleting task: {error}")
            return throw_error(status= status.HTTP_500_INTERNAL_SERVER_ERROR, message= "Internal Server Error", error_code= 500, error= error)
    
    
