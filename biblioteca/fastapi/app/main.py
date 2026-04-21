from fastapi import FastAPI
from app.database import Base, engine
from app.routers import books, users, loans
from app.models.book import Book
from app.models.user import User
from app.models.loan import Loan

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Gestor de Bibliotecas API",
    version="2.0.0"
)

app.include_router(books.router)
app.include_router(users.router)
app.include_router(loans.router)
