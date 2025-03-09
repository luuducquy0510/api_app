from sqlalchemy import Column, String
from .database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
    email = Column(String, primary_key=True, index=True, unique=True)
    username = Column(String, index=True, unique=True)
    fullname = Column(String)
    password = Column(String)


# class ChatHistory(Base):
#     __tablename__ = "chathistory"

