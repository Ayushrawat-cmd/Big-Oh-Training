from Models.user import User
from utils.logger import Logger
from Models.item import Item

logger = Logger.get_logger(__name__)

class UserService():
    __users = {}
    def __init__(self) -> None:
        self= self
    
    def getAllUsers(self):
        return self.__users
    
    def createUser(self, new_user: User):
        self.__users[new_user.id] = new_user
        return self.__users[new_user.id]
    
    def updateUser(self, user:User):
        if user.id not in self.__users:
            return None
        self.__users[user.id] = user
        return self.__users[user.id]    

    def deleteUser(self, oldUser: User):
        if oldUser.id not in self.__users:
            return None
        self.__users.pop(oldUser.id)
        
        return self.__users
    
    def addTask(self,userId:int, task:Item):
        if userId not in self.__users :
            return None
        self.__users[userId].task.append(task)
        return self.__users[userId]
    
    
