from pydantic import BaseModel, EmailStr 


# Authentication
class UserCreate(BaseModel):
    email: EmailStr
    username: str
    fullname: str
    password: str

class UserResponse(BaseModel):
    email: EmailStr
    username: str
    fullname: str
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
