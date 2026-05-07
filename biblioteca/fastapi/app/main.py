from fastapi import FastAPI

from app.database import Base, engine
from app.routers import books, users, loans
from app.models.book import Book
from app.models.user import User
from app.models.loan import Loan
from app.context_manager import LogFile

Base.metadata.create_all(bind=engine)

with LogFile("startup.log") as file:
    file.write("Sistema iniciado correctamente\n")

app = FastAPI(
    title="Gestor de Bibliotecas API",
    version="2.0.0"
)

app.include_router(books.router)
app.include_router(users.router)
app.include_router(loans.router)
