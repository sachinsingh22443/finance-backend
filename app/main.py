from fastapi import FastAPI
from app.database import engine, Base

from app.models import user
from app.models import transaction

app = FastAPI()

#  tables create 
Base.metadata.create_all(bind=engine)


#  routes import
from app.routes import user
from app.routes import transaction
from app.routes import dashboard

app.include_router(user.router)
app.include_router(transaction.router)
app.include_router(dashboard.router)


@app.get("/")
def root():
    return {"message": "Finance Backend Running 🚀"}