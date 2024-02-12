from utils.config import Config
from fastapi import FastAPI, HTTPException, Path
from typing import Annotated
import controller
# from controller import sample_controller, user_controller
from Models.item import Item
from fastapi_router_controller import Controller, ControllersTags
from fastapi.exceptions import RequestValidationError
from Service import sample_service

from utils.middleware import LogIncomingRequest, exception_handler, validation_exception_handler
# app = FastAPI(title="A sample application using fastapi_router_controller", version="0.1.0")
app = FastAPI(title='{}'.format(Config.read('app', 'name')),docs_url=Config.read('app', 'api-docs.path'),
    openapi_tags=ControllersTags)
# lists = {}

# @app.get("/")
# async def root():
#     return {"message":"Hello world!"}

# @app.get("/tasks")
# async def getTodoList() :
#     return {"tasks": lists}

# @app.put("/tasks/{task_id}")
# async def updateItem(item: Item, task_id: Annotated[int, Path(title="The ID of the item to get")]):
#     if task_id not in lists:
#         raise HTTPException(status_code=422, error="Item not found")
#     lists[task_id] = item
#     return {"message": "Task updated", "task": lists[task_id]}

# @app.post("/tasks")
# async def addNewItem(newItem: Item):
#     print(newItem)
#     lists[newItem.id] = newItem
#     return {"message":"Task created", "task": newItem}

# @app.delete("/tasks/{task_id}")
# async def deleteItem(task_id: Annotated[int, Path(title="The ID of the item to get")]):
#     if task_id not in lists:
#         raise HTTPException(status_code=422, detail="Item not found")
#     lists.pop(task_id)
#     return {"message":"Task deleted", "tasks": lists}
# routers = [sample_controller.controller.router]
app.exception_handler(RequestValidationError)(validation_exception_handler)

# configuring handler for generic error in order to format the response
app.exception_handler(Exception)(exception_handler)

# add middleware to process the request before it is taken by the router func
app.add_middleware(LogIncomingRequest)

# routers = [sample_controller.SampleController.router(), user_controller.UserController.router()]
# app.include_router(sample_controller.SampleController.router())
# app.include_router()
for router in Controller.routers():
    # print(router)
    app.include_router(router)
