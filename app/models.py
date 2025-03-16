from sqlalchemy import Column, String
from app import database
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy import Column, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship

class User(database.Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
    email = Column(String, primary_key=True, index=True, unique=True)
    username = Column(String, index=True, unique=True)
    password = Column(String)
    
    conversations = relationship("ChatHistory")


class ChatHistory(database.Base):
    __tablename__ = "chat_histories"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    chat_summary = Column(String, nullable=False)  # Store a summary of the chat
    created_at = Column(DateTime, default=func.now())

    # A chat history belongs to a user
    user = relationship("User")
    

