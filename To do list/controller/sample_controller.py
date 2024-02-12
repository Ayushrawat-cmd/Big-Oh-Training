from pathlib import Path
from fastapi_router_controller import Controller
from fastapi import Depends, HTTPException, status
from fastapi.responses import JSONResponse
from typing import Annotated,Optional
from schema.errors import Errors, ErrorModel, throw_error
from environment.Router import sample_router
from Models.item import Item
from Service.sample_service import SampleService
from utils.logger import Logger
from fastapi.encoders import jsonable_encoder
# router = APIRouter()
controller = Controller(sample_router)
logger = Logger.get_logger(__name__)
@controller.use()

@controller.resource()
class SampleController():
    def __init__(self, service:SampleService = Depends()) :
        self.service = service

    # @controller.route.get("/")
    # async def root():
    #     return {"message":"Hello world!"}

    @controller.route.get("", summary="fsfds")
    async def getTodoList(self) :
        # print(123)
        try:
            tasks = self.service.getAllTasks()
            if tasks is None:
                return Errors.HTTP_404_NOT_FOUND
            return  JSONResponse(status_code=status.HTTP_200_OK, content={"tasks": jsonable_encoder(tasks)})
        except Exception as error:
            logger.error(f"Error in getting item {error}")
            return throw_error(status= status.HTTP_500_INTERNAL_SERVER_ERROR, message= "Internal Server Error", error_code= 500, error= error)

    @controller.route.put("/{task_id}",responses={
            Errors.HTTP_404_NOT_FOUND.status_code: { 'model': ErrorModel, 'description': 'Item not found on DB' },
            Errors.HTTP_500_INTERNAL_SERVER_ERROR.status_code: { 'model': ErrorModel, 'description': 'Generic Error Occured' }
        })
    async def updateItem(self,item: Item, task_id: Annotated[int, Path(title="The ID of the item to get")]):
        try:
            update_item = self.service.updateTask(task_id, item)
            print(update_item)
            if update_item is None:
            # logger.error('Error getting item: {}'.format(error))
                return Errors.HTTP_404_NOT_FOUND
                # raise HTTPException(status_code=422, error="Item not found")
            return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content={"message": "Task updated", "task": jsonable_encoder(update_item)}) 
        except Exception as error:
            logger.error(f'Error updating item: {error}')
            return throw_error(status= status.HTTP_500_INTERNAL_SERVER_ERROR, message= "Internal Server Error", error_code= 500, error= error)

    @controller.route.post("", responses={
            Errors.HTTP_500_INTERNAL_SERVER_ERROR.status_code: { 
                'model': ErrorModel, 'description': 'Generic Error Occured' }
        })
    async def addNewItem(self, newItem: Item):
        try:
            item = self.service.insertTask(newItem)
            return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message":"Task created", "task":jsonable_encoder(item)})
            # return {"message":"Task created", "task": item}
        except Exception as error:
            logger.error(f'Error insterting task: {error}')
            return throw_error(status= status.HTTP_500_INTERNAL_SERVER_ERROR, message= "Internal Server Error", error_code= 500 , error= error)

    @controller.route.delete("/{task_id}",responses={
            Errors.HTTP_404_NOT_FOUND.status_code: { 'model': ErrorModel, 'description': 'Item not found on DB' },
            Errors.HTTP_500_INTERNAL_SERVER_ERROR.status_code: { 'model': ErrorModel, 'description': 'Generic Error Occured' }
        })
    async def deleteItem(self,task_id: Annotated[int, Path(title="The ID of the item to get")]):
        try:
            items = self.service.deleteTask(task_id)
            if items is None:
                return Errors.HTTP_404_NOT_FOUND
                # raise HTTPException(status_code=422, error="Item not found")
            return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content={"message":"Task deleted", "tasks": jsonable_encoder(items)}) 
        except Exception as error:
            logger.error(f"Error deleting task: {error}")
            return throw_error(status= status.HTTP_500_INTERNAL_SERVER_ERROR, message= "Internal Server Error", error_code= 500, error= error)