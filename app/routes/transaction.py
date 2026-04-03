from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate, TransactionResponse,TransactionUpdate
from app.utils.db import get_db
from app.utils.dependencies import get_current_role

router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.post("/", response_model=TransactionResponse)
def create_transaction(
    data: TransactionCreate,
    db: Session = Depends(get_db),
    role: str = Depends(get_current_role)
):
    if role != "admin":
        raise HTTPException(status_code=403, detail="Only admin can create")

    transaction = Transaction(**data.model_dump())

    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return transaction


@router.get("/", response_model=list[TransactionResponse])
def get_transactions(
    db: Session = Depends(get_db),
    role: str = Depends(get_current_role)
):
    if role not in ["admin", "analyst", "viewer"]:
        raise HTTPException(status_code=403, detail="Not allowed")

    return db.query(Transaction).all()


@router.put("/{id}")
def update_transaction(
    id: int,
    data: TransactionUpdate,
    db: Session = Depends(get_db),
    role: str = Depends(get_current_role)
):
    if role != "admin":
        raise HTTPException(status_code=403, detail="Only admin can update")

    transaction = db.query(Transaction).filter(Transaction.id == id).first()

    if not transaction:
        raise HTTPException(status_code=404, detail="Not found")

    #  ONLY updated fields change होंगे
    update_data = data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(transaction, key, value)

    db.commit()
    db.refresh(transaction)

    return transaction

@router.delete("/{id}")
def delete_transaction(
    id: int,
    db: Session = Depends(get_db),
    role: str = Depends(get_current_role)
):
    if role != "admin":
        raise HTTPException(status_code=403, detail="Only admin can delete")

    transaction = db.query(Transaction).filter(Transaction.id == id).first()

    if not transaction:
        raise HTTPException(status_code=404, detail="Not found")

    db.delete(transaction)
    db.commit()

    return {"message": "Deleted successfully"}


@router.get("/filter")
def filter_transactions(
    type: str = None,
    category: str = None,
    db: Session = Depends(get_db),
    role: str = Depends(get_current_role)
):
    query = db.query(Transaction)

    if type:
        query = query.filter(Transaction.type == type)

    if category:
        query = query.filter(Transaction.category == category)

    return query.all()