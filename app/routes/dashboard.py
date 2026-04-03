from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.transaction import Transaction
from app.utils.db import get_db
from app.utils.dependencies import get_current_role

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.transaction import Transaction
from app.utils.db import get_db
from app.utils.dependencies import get_current_role, allow_roles

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


#  Total Income
@router.get("/total-income")
def total_income(
    db: Session = Depends(get_db),
    role: str = Depends(allow_roles(["admin", "analyst"]))
):
    result = db.query(func.sum(Transaction.amount))\
        .filter(Transaction.type == "income").scalar()

    return {"total_income": result or 0}


#  Total Expense
@router.get("/total-expense")
def total_expense(
    db: Session = Depends(get_db),
    role: str = Depends(allow_roles(["admin", "analyst"]))
):
    result = db.query(func.sum(Transaction.amount))\
        .filter(Transaction.type == "expense").scalar()

    return {"total_expense": result or 0}


#  Balance
@router.get("/balance")
def balance(
    db: Session = Depends(get_db),
    role: str = Depends(allow_roles(["admin", "analyst"]))
):
    income = db.query(func.sum(Transaction.amount))\
        .filter(Transaction.type == "income").scalar() or 0

    expense = db.query(func.sum(Transaction.amount))\
        .filter(Transaction.type == "expense").scalar() or 0

    return {
        "income": income,
        "expense": expense,
        "net_balance": income - expense
    }


#  Category Summary
@router.get("/category-summary")
def category_summary(
    db: Session = Depends(get_db),
    role: str = Depends(allow_roles(["admin", "analyst"]))
):
    result = db.query(
        Transaction.category,
        func.sum(Transaction.amount).label("total")
    ).group_by(Transaction.category).all()

    return [
        {"category": r[0], "total": r[1]}
        for r in result
    ]


#  Recent Transactions
@router.get("/recent")
def recent_transactions(
    db: Session = Depends(get_db),
    role: str = Depends(allow_roles(["admin", "analyst"]))
):
    result = db.query(Transaction)\
        .order_by(Transaction.date.desc())\
        .limit(5).all()

    return result


#  Monthly Trends
@router.get("/monthly-trends")
def monthly_trends(
    db: Session = Depends(get_db),
    role: str = Depends(allow_roles(["admin", "analyst"]))
):
    result = db.query(
        func.extract("month", Transaction.date).label("month"),
        func.sum(Transaction.amount)
    ).group_by("month").all()

    return [
        {"month": int(r[0]), "total": r[1]}
        for r in result
    ]