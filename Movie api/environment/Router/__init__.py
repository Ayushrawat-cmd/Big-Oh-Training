from fastapi import APIRouter
import os

current_environ = os.environ.get('env_name')
__movie_path = os.environ.get('movie_controller')

movie_router = APIRouter(prefix='/movie')