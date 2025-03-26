from fastapi import FastAPI
from app.endpoints import llmchain, restaurant, orders, bookings, customer_support
from app.services.database import connect_db

app = FastAPI(title="Voice Agent API")

# Connect to MongoDB
connect_db()

# Include endpoints
app.include_router(llmchain.router, prefix="/api/llm")
app.include_router(restaurant.router, prefix="/api/restaurant")
app.include_router(orders.router, prefix="/api/orders")
app.include_router(bookings.router, prefix="/api/bookings")
app.include_router(customer_support.router, prefix="/api/support")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
