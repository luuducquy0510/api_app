from transformers import pipeline
import torch


device = "cuda" if torch.cuda.is_available() else "cpu"  # GPU if available, otherwise CPU

def chatbot_respone(system, assistant, user):
    messages = [
    {"role": "system", "content": system},
    {"role": "user", "content": assistant},
    {"role": "user", "content": user}
]
    # Load model on CUDA if available
    pipe = pipeline("text-generation", model="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B", device=device)

    # Run the model
    output = pipe(messages)

    return output