from pydantic import BaseModel, EmailStr 


# Authentication
class UserCreate(BaseModel):
    email: EmailStr
    username: str
    fullname: str
    password: str

class UserResponse(BaseModel):
    username: str
    fullname: str
    class Config():
        from_attributes = True
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


# llm app
class UserMessage(BaseModel):
    system: str
    assistant: str
    user: str