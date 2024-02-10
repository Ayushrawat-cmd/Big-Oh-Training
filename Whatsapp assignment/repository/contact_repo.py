from fastapi import Depends
from sqlalchemy.orm import Session

from utils.logger import Logger
from utils.db_connection import get_db_session
from models.user import Contact as ContactModel
# from models.user import User as UserModel
# from schema.contact_schema import ContactSchema
from schema.user_schema import UserSchema

logger = Logger.get_logger(__name__)
# print(logger)
class ContactRepository():
    def __init__(self, db_session:Session = Depends(get_db_session)) -> None:
        self.db = db_session
    
    async def read(self):
        logger.debug(f'Getting all contacts from db')
        return self.db.query(ContactModel).all()
    
    # def get_by_id(self, id):
    #     logger.debug(f'Getting user {id} from db')
    #     return self.db.query(UserModel).filter(UserModel.id == id).first()
    
    def getContactsOfUser(self,  userId: str):
        '''Get all contacts of the user from db'''
        db_contacts = self.db.query(ContactModel).filter(userId == ContactModel.user_id).all()
        return self.db.query(ContactModel).all()

    def insert(self,contact: UserSchema, userId:str):
        '''Inserting the user in the db'''
        logger.debug(f'Insert Contact {contact}')
        db_contact = self.db.query(ContactModel).filter(id == contact.id).first()
        print(db_contact,userId)
        if db_contact is None:
            db_contact = ContactModel(id=contact.id, name=contact.name, user_id = userId, phone_no = contact.phone_no, image = contact.image )
            self.db.add(db_contact)
        else:
            db_contact.user_id.append(userId)
        self.db.commit()
        self.db.refresh(db_contact)
        return db_contact
    
    def valid_contact(self, contactNo:str, userId:str):
        '''Is the given contact id exist by the userId'''        
        db_contact = self.db.query(ContactModel).filter(ContactModel.phone_no == contactNo).first()
        print(db_contact)
        if db_contact is None:
            return False
        return db_contact.user_id == userId
    
    # def delete(self, contactId:str, userId:str):
    #     '''Deleting the contact from the users contact list'''
    #     db_contact = self.db.query(ContactModel).filter(ContactModel.id == contactId).first()
    #     if db_contact is None:
    #         return None
    #     self.db
    # def delete(self, movieId):
    #     '''Delete query for the deleting movie from db'''
    #     db_movie = self.db.query(MovieModel).filter(MovieModel.id == movieId).first()
    #     # print(db_movie.id)
    #     if db_movie is None:
    #         return False
    #     logger.debug(f'Delete movie {db_movie}')
    #     self.db.delete(db_movie)
    #     self.db.commit()
    #     return True
    #     # self.db.refresh()

    # def update(self, movie: MovieSchema):
    #     '''Update the movie in the database'''
    #     logger.debug(f"Update movie {movie}")
    #     db_movie_query = self.db.query(MovieModel).filter(MovieModel.id == movie.id)
    #     db_movie = db_movie_query.first()
    #     if db_movie is None:
    #         return None
    #     db_movie.name = movie.name
    #     db_movie.image = movie.image
    #     db_movie.rating = movie.rating
    #     # db_movie_query.update(id = movie.id, name= movie.name)
    #     self.db.commit()
    #     self.db.refresh(db_movie)
        # return db_movie

        
