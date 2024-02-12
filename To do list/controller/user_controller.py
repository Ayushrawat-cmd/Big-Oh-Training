from pathlib import Path
from fastapi_router_controller import Controller
from fastapi import Depends, HTTPException, status
from fastapi.responses import JSONResponse
from typing import Annotated,Optional
from schema.errors import Errors, ErrorModel, throw_error
from environment.Router import user_router
from Models.user import User
from Models.item import Item
from Service.user_service import UserService
from utils.logger import Logger
from fastapi.encoders import jsonable_encoder

controller = Controller(user_router)
logger = Logger.get_logger(__name__)

@controller.use()
@controller.resource()
class UserController:
    def __init__(self, userService:UserService = Depends()) -> None:
        self.userService = userService
    
    @controller.route.get("", summary="fsfds")
    async def getAllUsers(self) :
        try:
            users = self.userService.getAllUsers()
            if users is None:
                return Errors.HTTP_404_NOT_FOUND
            return  JSONResponse(status_code=status.HTTP_200_OK, content={"users": jsonable_encoder(users)})
        except Exception as error:
            logger.error(f"Error in getting user {error}")
            return throw_error(status= status.HTTP_500_INTERNAL_SERVER_ERROR, message= "Internal Server Error", error_code= 500, error= error)
    
    @controller.route.post("")
    async def createUser(self, new_user:User):
        try:
            user = self.userService.createUser(new_user)
            return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message":"User created", "user":jsonable_encoder(user)})
        except Exception as error:
            logger.error(f"Error is creating user {error}")
            return throw_error(status= status.HTTP_500_INTERNAL_SERVER_ERROR, message= "Internal Server Error", error_code= 500, error= error)
    
    @controller.route.post("/{user_id}/task", responses={
            Errors.HTTP_500_INTERNAL_SERVER_ERROR.status_code: { 
                'model': ErrorModel, 'description': 'Generic Error Occured' }
        })
    async def addNewItem(self, newItem: Item, user_id: Annotated[int, Path(title="The ID of the user to get")]):
        try:
            user = self.userService.addTask(user_id,newItem)
            # item = self.service.insertTask(newItem)
            return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message":"Task created", "user":jsonable_encoder(user)})
            # return {"message":"Task created", "task": item}
        except Exception as error:
            logger.error(f'Error insterting task: {error}')
            return throw_error(status= status.HTTP_500_INTERNAL_SERVER_ERROR, message= "Internal Server Error", error_code= 500 , error= error)
    # @controller.route.put("/{userId}")
    # async def updateUser(self, )
    
