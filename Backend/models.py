from pydantic import BaseModel
class Item(BaseModel):
    name: str
    description: str
    quantity: int
    price: float

class User(BaseModel):
    user_id: int
    username: str
    role: str
    email: str
    password: str

class Transaction(BaseModel):
    transaction_id: int
    item_name: str
    user_id: int
    quantity:int
    transaction_type: str
    date: int