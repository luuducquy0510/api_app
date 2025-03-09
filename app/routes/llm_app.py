from fastapi import APIRouter
from .. import schemas, llm


router = APIRouter(
    tags = ["llm"]
)


@router.post("/chatbot")
def chatbot(message: schemas.UserMessage):
    reponse = llm.chatbot_respone(
        message.system,
        message.assistant,
        message.user
    )
    