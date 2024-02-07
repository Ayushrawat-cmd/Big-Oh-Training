from sqlalchemy import Column, String, NUMERIC
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from utils.db_connection import engine

class Base(DeclarativeBase):
    pass

class Movie(Base):
    __tablename__ = "Movie"
    id:Mapped[str] = mapped_column(primary_key=True, index=True)
    name:Mapped[str] = mapped_column(String(30), index=True) 
    rating:Mapped[int] = mapped_column(NUMERIC, index=True)
    image:Mapped[str] = mapped_column(String, index=True)

# Create the table in DB automatically, when this class is loaded
Base.metadata.create_all(bind=engine)