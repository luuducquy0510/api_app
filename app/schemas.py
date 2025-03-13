from pydantic import BaseModel, EmailStr 
from datetime import datetime
from uuid import UUID


# Authentication
class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

class UserResponse(BaseModel):
    email: EmailStr
    username: str
    
    class Config():
        from_attributes = True

# After login
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class User(BaseModel):
    id: UUID
    username: str
    email: str | None = None
    
    class Config():
        from_attributes = True
        
class UserInDB(User):
    hashed_password: str
    
class TokenData(BaseModel):
    email: str | None = None

# llm app
class UserMessage(BaseModel):
    system: str
    assistant: str
    user: str
    
class ChatOutput(BaseModel):
    chat_summary: str
    created_at: datetime