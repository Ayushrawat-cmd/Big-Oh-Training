from fastapi import Depends
from schema.user_schema import UserSchema
from utils.logger import Logger
from repository.user_repo import UserRepository
# from Models.item import Item

logger = Logger.get_logger(__name__)

class UserService():

    def __init__(self, repository: UserRepository = Depends()) -> None:
        self.repository = repository
    
    def getUserById(self, userId):
        '''Get the user by the id'''
        return self.repository.get_by_id(userId)

    def getAllUsers(self):
        '''Get all the users from the db'''
        logger.debug("Getting all users from db")
        return self.repository.read()
    
    def createUser(self, new_user: UserSchema):
        '''Create user in the db'''
        logger.debug(f'Insert new-user {new_user}')
        return self.repository.insert(new_user)

    # def addContact(self, new_contact :UserSchema, userId :str):
    #     if self.repository.get_by_id(userId) is None:
    #         return None
    #     self.repository.addContact(new_contact, userId)
    # def updateMovie(self, movie:MovieSchema):
    #     '''update movie in the db'''
    #     logger.debug(f'Update movie {movie}')
    #     return self.repository.update(movie)

    def deletUser(self, oldUserID):
        '''delete movie from the db'''
        # print(oldMovieID)
        return self.repository.delete(oldUserID)

    
    # def addTask(self,userId:int, task:Item):
    #     if userId not in self.__users :
    #         return None
    #     self.__users[userId].task.append(task)
    #     return self.__users[userId]
    
    
