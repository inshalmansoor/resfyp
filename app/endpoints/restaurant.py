from fastapi import APIRouter

router = APIRouter()

@router.get("/info")
async def get_restaurant_info():
    # You can either directly call the tool or
    # route this request through the LLM chain.
    return {"menu": "Example menu", "locations": ["Location1", "Location2"]}
