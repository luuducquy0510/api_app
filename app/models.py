from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
    __tablename__ = "users"

    email = Column(String, primary_key=True, index=True, unique=True)
    username = Column(String, index=True, unique=True)
    fullname = Column(String)
    password = Column(String)

   