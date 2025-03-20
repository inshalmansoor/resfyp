from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_reservations():
    """
    Dummy endpoint for retrieving reservations.
    """
    return {"reservations": []}

@router.post("/")
def book_reservation(reservation: dict):
    """
    Dummy endpoint for booking a reservation.
    """
    # In a real app, this would add the reservation to MongoDB.
    return {"message": "Reservation booked successfully.", "reservation": reservation}
