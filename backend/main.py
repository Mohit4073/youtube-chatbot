from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chatbot import get_video_response  # your chatbot logic function

app = FastAPI()

# ✅ CORS support for Chrome extension
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev. You can replace with chrome-extension://<EXTENSION_ID> later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Request body model
class ChatRequest(BaseModel):
    video_id: str
    query: str

# ✅ Chat route
@app.post("/chat")
def chat_api(req: ChatRequest):
    return {"response": get_video_response(req.video_id, req.query)}
