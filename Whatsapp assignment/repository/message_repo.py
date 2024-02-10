from fastapi import Depends
from sqlalchemy.orm import Session

from utils.logger import Logger
from utils.db_connection import get_db_session
from models.user import Message as MessageModel
from models.user import User as UserModel
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

    def read(self):
        logger.debug(f'Getting all messages from db')
        return self.db.query(MessageModel).all()
    
    def read_recieved_messages(self, reciever_id:str ):
        reciever = self.db.query(UserModel).filter(reciever_id == UserModel.id).first()
        if reciever is None:
            return None
        msgs = self.db.query(MessageModel).filter(reciever.phone_no == MessageModel.reciever_phn_no).all()
        if msgs is None:
            return None
        return msgs
    
    def read_sent_messages(self, senderId: str):
        msgs= self.db.query(MessageModel).filter(senderId == MessageModel.sender_id).all()
        print(msgs)
        if msgs is None:
            return None
        return msgs

    def insert(self,message:Union[TextSchema, AudioSchema, VideoSchema], senderId :str):
        '''Inserting the Message in the db'''
        logger.debug(f'Insert Message {message}')
        model = message.__class__.__name__.split('Schema')[0]
        print(model)
        content = None
        # db_message = None
        if isinstance(message, TextSchema):
            content = message.description
        elif isinstance(message, AudioSchema):
            content = message.audioClip
        elif isinstance(message, VideoSchema):
            content = message.videoUrl
        db_message = TypeOfMessageModels[model](id=message.id,  sender_id =senderId, reciever_phn_no =message.reciever_phone_no, content=content)
        # db_user = UserModel(id = user.id, name=user.name, phone_no = user.phone_no, image = user.image)
        # self.db.add(db_user)
        self.db.add(db_message)
        self.db.commit()
        self.db.refresh(db_message)
        return db_message
