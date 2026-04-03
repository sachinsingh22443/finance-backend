from pydantic import BaseModel
from datetime import date

class TransactionCreate(BaseModel):
    amount: float
    type: TransactionType
    category: CategoryEnum
    date: date
    notes: str

class TransactionResponse(BaseModel):
    id: int
    amount: float
    type: str
    category: str
    date: date
    notes: str

    class Config:
        from_attributes = True
        
 
from enum import Enum

class TransactionType(str, Enum):
    income = "income"
    expense = "expense"  
    
class CategoryEnum(str, Enum):
    salary = "salary"
    food = "food"
    rent = "rent"
    shopping = "shopping"     
from pydantic import BaseModel
from datetime import date
from typing import Optional

class TransactionUpdate(BaseModel):
    amount: Optional[float] = None
    type: Optional[str] = None
    category: Optional[str] = None
    date: Optional[date] = None
    notes: Optional[str] = None
    