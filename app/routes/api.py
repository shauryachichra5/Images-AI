import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from services.bot_reply import bot_reply

router = APIRouter()

@router.post("/get_reply")
async def api_get_reply(data: dict):
    user_message = data.get("message", "")
    reply, images = bot_reply(user_message)
    
    return JSONResponse({"reply": reply, "images_dict": images})
