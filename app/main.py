from fastapi import FastAPI
from .routes import authen


app = FastAPI()

# Authentication
app.include_router(authen.router)

