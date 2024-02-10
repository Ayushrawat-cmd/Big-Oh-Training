from fastapi import Depends
from repository.contact_repo import ContactRepository
class ContactValidatorService:
    def __init__(self, contactRepository: ContactRepository = Depends()) -> None:
        self.repository = contactRepository

    def isContactExist(self, contactNo: str, userID:str):
        return self.repository.valid_contact(contactNo, userID)
    