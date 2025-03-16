from fastapi import APIRouter, Depends, UploadFile
from app import llm_config, schemas, auth, models, database, utils
from typing import Annotated
from sqlmodel import Session
import os
import shutil


router = APIRouter(
    tags=["LLM"]
)

UPLOAD_FOLDER = "./data"

@router.post("/upload")
async def upload_pdf(file: UploadFile,
                     current_user: Annotated[schemas.User, Depends(auth.get_current_user)]):
    # Ensure the uploaded file is a PDF
    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDF files are allowed!"}

    # Define file path
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    # Save the file locally
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": "PDF uploaded successfully", "filename": file.filename, "path": file_path}


@router.post("/summarize")
def summarize(current_user: Annotated[schemas.User, Depends(auth.get_current_user)]):
    pages = utils.load_latest_pdf(UPLOAD_FOLDER)
    result = llm_config.get_results(pages)
    os.remove(utils.get_latest_path(UPLOAD_FOLDER))
    chat_obj = models.ChatHistory(
        user_id = current_user.id,
        chat_summary = result.chat_summary,
        created_at = result.created_at
    )
    with Session(database.engine) as session:
        session.add(chat_obj)
        session.commit()
        session.refresh(chat_obj)
       
    return chat_obj.chat_summary
