from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.ai_wrapper import process_prompt

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str
    user_id: str
    mode: str

class AIResponse(BaseModel):
    response: str

@router.post("/submit_prompt", response_model=AIResponse)
async def submit_prompt(req: PromptRequest):
    try:
        reply = await process_prompt(req.prompt, req.mode, req.user_id)
        return AIResponse(response=reply)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
