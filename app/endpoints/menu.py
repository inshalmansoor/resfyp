from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_menu():
    """
    Dummy endpoint for retrieving menu items.
    """
    # In a real implementation, you might fetch this from your knowledge base or database.
    dummy_menu = [
        {"id": 1, "name": "Margherita Pizza", "price": 10.99},
        {"id": 2, "name": "Caesar Salad", "price": 7.99},
    ]
    return {"menu": dummy_menu}

@router.post("/item")
def add_menu_item(item: dict):
    """
    Dummy endpoint for adding a new menu item.
    """
    # Logic to add item to the database goes here.
    return {"message": "Menu item added successfully.", "item": item}
