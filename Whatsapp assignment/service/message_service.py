from fastapi import Depends
from schema.user_schema import UserSchema
from utils.logger import Logger
# from repository.user_repo import UserRepository
from repository.message_repo import MessageRepository
# from Models.item import Item
from schema.message_schema import AudioSchema, TextSchema, VideoSchema
from typing import Union
from service.contact_validator import ContactValidatorService
logger = Logger.get_logger(__name__)

class MessageService():

    def __init__(self, repository: MessageRepository = Depends(), contactValidation:ContactValidatorService = Depends() ) -> None:
        self.repository = repository
        self.contactValidationService = contactValidation
    
    # def getUserById(self, userId):
    #     '''Get the user by the id'''
    #     return self.repository.get_by_id(userId)

    # def getAllUsers(self):
    #     '''Get all the users from the db'''
    #     logger.debug("Getting all users from db")
    #     return self.repository.read()
    
    def sendMessage(self, msg:Union[ AudioSchema, TextSchema, VideoSchema], senderId: str):
        '''Send the audio message'''
        logger.debug(f'Sending message {msg}')
        # if self.contactValidationService.isContactExist(msg.recieverId, senderId):
        return self.repository.insertAudioMessage(msg,senderId)
        # return False
    
    # def sendTextMessage(self, msg:TextSchema, senderId:)

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
    
    
