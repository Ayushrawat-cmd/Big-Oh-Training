from fastapi import APIRouter
import os

current_environ = os.environ.get('env_name')
__user_path = os.environ.get('user_controller')

user_router = APIRouter(prefix='/user')
message_router = APIRouter(prefix='/user')
contact_router = APIRouter(prefix='/user')