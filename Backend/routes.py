from fastapi import APIRouter, HTTPException
from database import items_collection, users_collection, transactions_collection
from models import Item, User, Transaction
from datetime import datetime
from typing import List
from bson import ObjectId


router = APIRouter()

@router.post("/items/")
async def Create_item(item : Item):
    result = await items_collection.insert_one(item.dict())
    return {"id": str(result.inserted_id), "message": "added"}


@router.post("/items/bulk/", tags=["Items"])
async def create_items(items: List[Item]):
    items_data = [item.dict() for item in items]
    result = await items_collection.insert_many(items_data)

    return {"ids" : [str(id) for id in result.inserted_ids], "message" : "added"}


@router.post("/users/bulk/", summary="Bulk Insert Users", tags=["Users"])
async def create_users(users: List[User]):
    if not users:
        raise HTTPException(status_code=400, detail="No users provided")
    users_data = [user.dict() for user in users]
    result = await users_collection.insert_many(users_data)
    return {
        "inserted_ids": [str(id) for id in result.inserted_ids],
        "message": "Users added successfully"
    }

@router.post("/transactions/bulk/", summary="Bulk Insert Transactions", tags=["Transactions"])
async def create_transactions(transactions: List[Transaction]):
    if not transactions:
        raise HTTPException(status_code=400, detail="No transactions provided")
    transactions_data = []
    for transaction in transactions:
        # Convert date from string to datetime object
        transaction_data = transaction.dict()
        if isinstance(transaction_data['date'], str):
            # Convert the date from string (if necessary) to datetime object
            transaction_data['date'] = datetime.strptime(transaction_data['date'], "%Y-%m-%d")
        transactions_data.append(transaction_data)

    try:
        result = await transactions_collection.insert_many(transactions_data)
        return {
            "inserted_ids": [str(id) for id in result.inserted_ids],
            "message": "Transactions added successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error inserting transactions: {str(e)}")


@router.put("/items/name/{item_name}/", summary="Update Item by Name", tags=["Items"])
async def update_item_by_name(item_name: str, item: Item):
    # Convert the item data into a dictionary
    item_data = item.dict()
    result = await items_collection.update_one(
        {"name": item_name},  # Find the item by its name
        {"$set": item_data}  # Update the fields
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail=f"Item with name '{item_name}' not found")
    return {"message": f"Item with name '{item_name}' updated successfully"}





@router.put("/users/{user_id}/", summary="Update User by ID", tags=["Users"])
async def update_user(user_id: int, user: User):
    # Update user in the database by user_id
    user_data = user.dict()
    result = await users_collection.update_one(
        {"user_id": user_id},
        {"$set": user_data}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User updated successfully"}

# Update Transaction by ID
@router.put("/transactions/{transaction_id}/", summary="Update Transaction by ID", tags=["Transactions"])
async def update_transaction(transaction_id: int, transaction: Transaction):
    # Update transaction in the database by transaction_id
    transaction_data = transaction.dict()
    result = await transactions_collection.update_one(
        {"transaction_id": transaction_id},
        {"$set": transaction_data}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return {"message": "Transaction updated successfully"}






@router.delete("/users/{user_id}/", summary="Delete User by ID", tags=["Users"])
async def delete_user(user_id: int):
    result = await users_collection.delete_one({"user_id": user_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

# Delete Transaction by ID
@router.delete("/transactions/{transaction_id}/", summary="Delete Transaction by ID", tags=["Transactions"])
async def delete_transaction(transaction_id: int):
    result = await transactions_collection.delete_one({"transaction_id": transaction_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return {"message": "Transaction deleted successfully"}


@router.get("/items/count")
async def get_items_count():
    # Get the count of items in the database
    total_items = await items_collection.count_documents({})
    return {"total_items": total_items}

@router.get("/transactions/count")
async def get_transactions_count():
    # Get the count of transactions in the database
    total_transactions = await transactions_collection.count_documents({})
    return {"total_transactions": total_transactions}

# Helper function to convert ObjectId to string
def str_object_id(document):
    if isinstance(document, dict):
        for key, value in document.items():
            if isinstance(value, ObjectId):
                document[key] = str(value)
            elif isinstance(value, dict):
                document[key] = str_object_id(value)
    return document

@router.get("/items/")
async def get_items():
    items_cursor = items_collection.find()
    items = await items_cursor.to_list(length=None)  # Fetch all items from the collection

    # Convert ObjectId to string
    items = [str_object_id(item) for item in items]

    return items

@router.get("/transactions/")
async def get_transactions():
    transactions_cursor = transactions_collection.find()
    transactions = await transactions_cursor.to_list(length=None)  # Fetch all transactions

    # Convert ObjectId to string
    transactions = [str_object_id(transaction) for transaction in transactions]

    return transactions