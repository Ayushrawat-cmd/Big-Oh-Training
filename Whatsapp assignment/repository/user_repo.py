from fastapi import Depends
from sqlalchemy.orm import Session

from utils.logger import Logger
from utils.db_connection import get_db_session
from models.user import User as UserModel
from repository.contact_repo import ContactRepository
from schema.user_schema import UserSchema

logger = Logger.get_logger(__name__)
# print(logger)
class UserRepository():
    def __init__(self, db_session:Session = Depends(get_db_session), contactRepo: ContactRepository =Depends()) -> None:
        print("dsad")
        self.db = db_session
        self.contact_repo = contactRepo
    def read(self):
        logger.debug(f'Getting all users from db')
        return self.db.query(UserModel).all()
    
    def get_by_id(self, id):
        logger.debug(f'Getting user {id} from db')
        return self.db.query(UserModel).filter(UserModel.id == id).first().recievedMessages

    def getSentMessage(self, id):
        logger.debug(f'Getting sent messages by user {id} from db')
        return self.db.query(UserModel).filter(UserModel.id == id).first().sentMessages
    
    def getRecievedMessage(self, id):
        logger.debug(f'Getting recieved messages by user {id} from db')
        return self.db.query(UserModel).filter(UserModel.id == id).first().recievedMessages

    def getContactsOfUser(self, id):
        logger.debug(f'Getting contacts of user {id} from db')
        return self.db.query(UserModel).filter(UserModel.id == id).first().contacts
    
    def insert(self,user: UserSchema):
        '''Inserting the user in the db'''
        logger.debug(f'Insert User {user}')
        db_user = UserModel(id = user.id, name=user.name, phone_no = user.phone_no, image = user.image)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def delete(self, userId):
        '''Delete query for the deleting movie from db'''
        db_user = self.db.query(UserModel).filter(UserModel.id == userId).first()
        # print(db_movie.id)
        if db_user is None:
            return False
        logger.debug(f'Delete user {db_user}')
        self.db.delete(db_user)
        self.db.commit()
        return True
        # self.db.refresh()

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

        
