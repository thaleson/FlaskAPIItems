from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from .models import Item as DBItem
from schemas import Item as ItemSchema, ItemCreate
from .database import SessionLocal, engine

app = FastAPI()

"""
FastAPI application for managing items.

This application provides CRUD (Create, Read, Update, Delete) operations for items
using SQLAlchemy for ORM and Pydantic for data validation.

Endpoints:
- POST /items/:
    Create a new item. Expects a JSON payload with 'name' and 'description'.
    Returns the created item.

- GET /items/{item_id}:
    Retrieve an item by its ID. Returns the item if found, otherwise raises a 404 error.

- GET /items/:
    Retrieve a list of all items. Returns a list of items.

- PUT /items/{item_id}/:
    Update an existing item by its ID. Expects a JSON payload with 'name' and 'description'.
    Returns the updated item if successful, otherwise raises a 404 error.

- DELETE /items/{item_id}/:
    Delete an item by its ID. Returns the deleted item if successful, otherwise raises a 404 error.

Dependencies:
- `get_db()`: Provides a SQLAlchemy database session for handling requests.

Models:
- `ItemCreate`: Schema used for creating and updating items.
- `ItemSchema`: Schema used for representing items with their ID.

Dependencies:
- SQLAlchemy's SessionLocal for database sessions.
- Pydantic for data validation and serialization.
"""

# Dependency
def get_db():
    """
    Provides a SQLAlchemy database session for handling requests.

    Yields:
        Session: A SQLAlchemy session object.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/items/", response_model=ItemSchema)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    """
    Create a new item.

    Args:
        item (ItemCreate): The item to be created.
        db (Session): The SQLAlchemy session.

    Returns:
        ItemSchema: The created item.
    """
    db_item = DBItem(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/items/{item_id}", response_model=ItemSchema)
def read_item(item_id: int, db: Session = Depends(get_db)):
    """
    Retrieve an item by its ID.

    Args:
        item_id (int): The ID of the item to retrieve.
        db (Session): The SQLAlchemy session.

    Returns:
        ItemSchema: The item if found.

    Raises:
        HTTPException: If the item is not found.
    """
    db_item = db.query(DBItem).filter(DBItem.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.get("/items/", response_model=list[ItemSchema])
def read_items(db: Session = Depends(get_db)):
    """
    Retrieve a list of all items.

    Args:
        db (Session): The SQLAlchemy session.

    Returns:
        list[ItemSchema]: A list of all items.
    """
    items = db.query(DBItem).all()
    return items

@app.put("/items/{item_id}/", response_model=ItemSchema)
def update_item(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    """
    Update an existing item by its ID.

    Args:
        item_id (int): The ID of the item to update.
        item (ItemCreate): The new item data.
        db (Session): The SQLAlchemy session.

    Returns:
        ItemSchema: The updated item.

    Raises:
        HTTPException: If the item is not found.
    """
    db_item = db.query(DBItem).filter(DBItem.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.name = item.name
    db_item.description = item.description
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/items/{item_id}/", response_model=ItemSchema)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """
    Delete an item by its ID.

    Args:
        item_id (int): The ID of the item to delete.
        db (Session): The SQLAlchemy session.

    Returns:
        ItemSchema: The deleted item.

    Raises:
        HTTPException: If the item is not found.
    """
    db_item = db.query(DBItem).filter(DBItem.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return db_item
