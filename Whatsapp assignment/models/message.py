from sqlalchemy import Column, String, NUMERIC,ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column,relationship,Relationship,backref
from utils.db_connection import engine
from typing import List, Optional
# from pydantic import BaseModel
# from models.user import UserM
class Base(DeclarativeBase):
    pass

class Message(Base):
    __tablename__ = "message"
    id:Mapped[str] = mapped_column(primary_key=True, index=True)
    type:Mapped[str] = mapped_column(nullable=False)
    sender_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    reciever_id :Mapped[str] = mapped_column(ForeignKey("users.id"))
    sender: Mapped["User"] = relationship(back_populates="sentMessages")
    reciever : Mapped["User"] = relationship(back_populates="recievedMessage")
    content:Mapped[str] = mapped_column(String(30)) 
    __mapper_args__ = {
        "polymorphic_on": "type",
        "polymorphic_identity": "message",
    }

class Audio(Message):
    __tablename__ = "audio"
    id: Mapped[str] = mapped_column(ForeignKey("message.id"), primary_key=True)
    content:Mapped[str] = mapped_column(String(100)) 
    __mapper_args__ = {
        "polymorphic_identity": "audio", 
    }

class Text(Message):
    __tablename__ = "text"
    id: Mapped[str] = mapped_column(ForeignKey("message.id"), primary_key=True)
    content:Mapped[str] = mapped_column(String(100))
    __mapper_args__ = {
        "polymorphic_identity": "text", 
    }

class Video(Message):
    __tablename__ = "video"
    id: Mapped[str] = mapped_column(ForeignKey("message.id"), primary_key=True)
    content:Mapped[str] = mapped_column(String(100))
    __mapper_args__ = {
        "polymorphic_identity": "video", 
    }