from fastapi import APIRouter
import os

current_environ = os.environ.get('env_name')
__sample_path = os.environ.get('sample_controller')
__user_path = os.environ.get('user_controller')

print(current_environ)
sample_router = APIRouter(prefix=__sample_path)
user_router = APIRouter(prefix=__user_path)