from sqlalchemy import Column, String, NUMERIC,ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column,relationship,Relationship,backref
from utils.db_connection import engine
from typing import List, Optional
# from models.message import Message
# from models.contact import Contact
class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id:Mapped[str] = mapped_column(primary_key=True, index=True)
    name:Mapped[str] = mapped_column(String(30)) 
    phone_no:Mapped[str] = mapped_column(String(10))
    image:Mapped[str] = mapped_column(String)
    contacts:Mapped[List["Contact"]] = relationship(back_populates='user',foreign_keys='Contact.user_id')
    sentMessages:Mapped[List["Message"]] = relationship(back_populates="sender", foreign_keys='Message.sender_id')
    recievedMessages:Mapped[List["Message"]] = relationship(back_populates="reciever", foreign_keys='Message.reciever_phn_no')
    # __mapper_args__ = {
    #     "polymorphic_on": "type",
    #     "polymorphic_identity": "message",
    # }
#     user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
#     contacts: Mapped[Optional[List["User"]]] = Relationship(
#     sa_relationship_kwargs=dict(
#       cascade="all",
#       backref=backref("user", remote_side="User.id"),
#     )  
#   )
    # user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    # user: Mapped["User"] = relationship(back_populates="contacts")
# class Contact(Base):
#     __tablename__ ="contacts"
#     id:Mapped[str] = mapped_column(ForeignKey('users.id'), primary_key=True)
#     # name:Mapped[str] = mapped_column(String(30)) 
#     # phone_no:Mapped[str] = mapped_column(String(10))
#     # image:Mapped[str] = mapped_column(String)
#     user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
#     user: Mapped["User"] = relationship(back_populates="contacts")

class Contact(Base):
    __tablename__ ="contacts"
    id:Mapped[str] = mapped_column(primary_key=True, index=True)
    name:Mapped[str] = mapped_column(String(30)) 
    phone_no:Mapped[str] = mapped_column(String(10))
    image:Mapped[str] = mapped_column(String)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="contacts")
# Create the table in DB automatically, when this class is loaded
class Message(Base):
    __tablename__ = "message"
    id:Mapped[str] = mapped_column(primary_key=True, index=True)
    type:Mapped[str] = mapped_column(nullable=False)
    sender_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    reciever_phn_no :Mapped[str] = mapped_column(ForeignKey("users.phone_no"))
    sender: Mapped["User"] = relationship(back_populates="sentMessages", foreign_keys=[sender_id])
    reciever : Mapped["User"] = relationship(back_populates="recievedMessages", foreign_keys=[reciever_phn_no])
    # content:Mapped[str] = mapped_column(String(30)) 
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
Base.metadata.create_all(bind=engine)