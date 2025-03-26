# app/endpoints/llmchain.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.llm import process_llm_chain

router = APIRouter()

class LLMRequest(BaseModel):
    input_text: str

@router.post("/")
async def invoke_llmchain(payload: LLMRequest):
    try:
        input_text = payload.input_text
        print(f"input_text --> {input_text}")
        result = process_llm_chain(input_text)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))






