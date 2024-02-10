from fastapi import Depends
from sqlalchemy.orm import Session

from utils.logger import Logger
from utils.db_connection import get_db_session
from models.user import User as UserModel
# from models.user import 
from repository.contact_repo import ContactRepository
from schema.user_schema import UserSchema
from models.user import Message as MessageModel
from models.user import Audio as AudioModel
from models.user import Text as TextModel
from models.user import Video as VideoModel
from schema.message_schema import MessageSchema, AudioSchema, TextSchema,VideoSchema
from typing import Union
logger = Logger.get_logger(__name__)
# print(logger)
TypeOfMessageModels ={
    'Audio':AudioModel,
    'Text':TextModel,
    'Video':VideoModel
}
class MessageRepository():
    db = None
    def __init__(self, db_session:Session = Depends(get_db_session)) -> None:
        # if self is None:
        self.db = db_session
        # else:
        #     self =self
        
        # self.contact_repo = contactRepo
    def read(self):
        logger.debug(f'Getting all messages from db')
        return self.db.query(MessageModel).all()
    
    # def get_by_id(self, id):
    #     logger.debug(f'Getting user {id} from db')
    #     return self.db.query(UserModel).filter(UserModel.id == id).first()

    # def getContactsOfUser(self, id):
        # logger.debug(f'Getting contacts of user {id} from db')
        # return self.db.query(UserModel).filter(UserModel.id == id).first().contacts
    
    def insertAudioMessage(self, audio:AudioSchema, senderId:str):
        '''Inserting the Message in the db'''
        print(3213)
        logger.debug(f'Insert Message {audio}')
        db_audio_message = AudioModel(id=audio.id,  sender_id =senderId, reciever_id =audio.recieverId, content=audio.content)
        self.db.add(db_audio_message)
        self.db.commit()
        self.db.refresh(db_audio_message)
        return db_audio_message

    def insert(self,message:Union[TextSchema, AudioSchema, VideoSchema], senderId :str):
        '''Inserting the Message in the db'''
        logger.debug(f'Insert Message {message}')
        model = message.__class__.__name__.split('Schema')[0]
        print(model)
        db_message = TypeOfMessageModels[model](id=message.id,  senderId =senderId, recieverId =message.recieverId, content=message.content)
        # db_user = UserModel(id = user.id, name=user.name, phone_no = user.phone_no, image = user.image)
        # self.db.add(db_user)
        self.db.add(db_message)
        self.db.commit()
        self.db.refresh(db_message)
        return db_message

    # def addContact(self, contact:UserSchema, userId: str):
    #     '''Inserting the contact for the given user in the db'''
    #     db_user = self.db.query(UserModel).filter(UserModel.id == userId).first()
    #     db_contact =self.db.query(UserModel).filter(UserModel.id == contact.id).first() 
    #     if db_contact is None:
    #         db_contact = self.contact_repo.insert(contact, userId)            

    #     db_user.contacts.append(db_contact)
    #     self.db.commit()
    #     self.db.refresh(db_user)
        
    # def delete(self, userId):
    #     '''Delete query for the deleting movie from db'''
    #     db_user = self.db.query(UserModel).filter(UserModel.id == userId).first()
    #     # print(db_movie.id)
    #     if db_user is None:
    #         return False
    #     logger.debug(f'Delete user {db_user}')
    #     self.db.delete(db_user)
    #     self.db.commit()
    #     return True
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

        
