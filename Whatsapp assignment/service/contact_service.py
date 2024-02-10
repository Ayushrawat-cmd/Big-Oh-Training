from fastapi import Depends
# from schema.contact_schema import ContactSchema
from utils.logger import Logger
# from repository.user_repo import UserRepository
from schema.user_schema import UserSchema
from repository.contact_repo import ContactRepository
# from Models.item import Item

logger = Logger.get_logger(__name__)

class ContactService():
    def __init__(self, ContactRepository:ContactRepository = Depends()) -> None:
        self.repository =ContactRepository
    
    def addContact(self, new_contact :UserSchema, userId :str):
        # if self.repository.get_by_id(userId) is None:
        #     return None
        return self.repository.insert(new_contact, userId)
    
    def getContacts(self,  userId: str):
        '''Get contacts of the user'''
        return self.repository.getContactsOfUser(userId)
