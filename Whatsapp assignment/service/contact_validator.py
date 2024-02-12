from fastapi import Depends
from repository.user_repo import UserRepository
class ContactValidatorService:
    def __init__(self, userRepository: UserRepository = Depends()) -> None:
        self.repository = userRepository

    def isContactExist(self, contactNo: str, userID:str):
        return self.repository.valid_contact(contactNo, userID)
    