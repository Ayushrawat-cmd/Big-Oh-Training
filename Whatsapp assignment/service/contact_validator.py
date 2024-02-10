from fastapi import Depends
from repository.contact_repo import ContactRepository
class ContactValidatorService:
    def __init__(self, contactRepository: ContactRepository = Depends()) -> None:
        self.repostiory = contactRepository

    def isContactExist(self, contactId: str, userID:str):
        return self.repostiory.valid_contact(contactId, userID)
    