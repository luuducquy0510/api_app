from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from app import schemas, auth, models, database
from sqlmodel import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


router = APIRouter(
    tags=["Authentication"],
)


# @router.post("/create")
def create_account(accounts: schemas.UserCreate):
    hashed_password = auth.hash_password(accounts.password)
    db_acc = models.User(
        email=accounts.email, 
        username=accounts.username, 
        password=hashed_password
    )
    with Session(database.engine) as session:
        session.add(db_acc)
        session.commit()
        session.refresh(db_acc)
    return schemas.UserResponse(
        username=db_acc.username,
        email = db_acc.email
    )
         
# Check if account already exist
@router.post("/register", response_model=schemas.UserResponse)
def register_account(account: schemas.UserCreate):
    db_acc = auth.get_user_by_email(account.email)
    if db_acc:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_account(account)

# Login (returns JWT token)
@router.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = auth.get_user_by_email(form_data.username)
    
    if not user or not auth.verify_password(form_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token = auth.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


