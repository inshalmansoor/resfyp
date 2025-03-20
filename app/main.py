from fastapi import FastAPI
from app.endpoints import (
    customer_support,
    menu,
    issues,
    feedback,
    complaints,
    reservations,
    orders,
)

app = FastAPI(title="Restaurant Voice Agent")

# Include routers with appropriate prefixes
app.include_router(customer_support.router, prefix="/support", tags=["Customer Support"])
app.include_router(menu.router, prefix="/menu", tags=["Menu"])
app.include_router(issues.router, prefix="/issues", tags=["Issues"])
app.include_router(feedback.router, prefix="/feedback", tags=["Feedback"])
app.include_router(complaints.router, prefix="/complaints", tags=["Complaints"])
app.include_router(reservations.router, prefix="/reservations", tags=["Reservations"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])

# Optional: Dummy endpoint for microphone access
@app.get("/mic", tags=["Microphone"])
def microphone_access():
    """
    Dummy endpoint for microphone access integration.
    """
    return {"message": "Microphone access endpoint - integration pending."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
