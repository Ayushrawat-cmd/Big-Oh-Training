import controller
from controller.movie_controller import MovieController
from utils.config import Config
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi_router_controller import Controller, ControllersTags
from utils.middleware import LogIncomingRequest, exception_handler, validation_exception_handler

app = FastAPI(
    title='{}'.format(Config.read('app', 'name')),
    description='This is a very fancy project, with auto docs for the API and everything',
    version='0.0.1',
    openapi_tags=ControllersTags)


app.exception_handler(RequestValidationError)(validation_exception_handler)

# configuring handler for generic error in order to format the response
app.exception_handler(Exception)(exception_handler)

# add middleware to process the request before it is taken by the router func
app.add_middleware(LogIncomingRequest)

# for router in Controller.routers():
app.include_router(MovieController.router())
