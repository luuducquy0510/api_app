from datetime import datetime
import os
from dotenv import load_dotenv
from app import schemas
import google.generativeai as genai


load_dotenv()
api_key = os.getenv("Gemini_API")

def user_message(docs):
    return f"""
            "You are an expert in Natural Language Processing. Your task is to summarize the provided content in bullet points.

            "content": {docs}

            """

def get_results(pages):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    current_time = datetime.now()
    response_message = model.generate_content(user_message(pages)).text

    return schemas.ChatOutput(chat_summary=response_message, created_at=current_time)

