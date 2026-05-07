from datetime import datetime

from app.repositories.book_repository import BookRepository
from app.repositories.user_repository import UserRepository
from app.repositories.loan_repository import LoanRepository
from app.exceptions.custom_exceptions import (
    BookNotFoundError,
    BookNotAvailableError,
    UserNotFoundError,
    LoanNotFoundError,
    LoanAlreadyReturnedError,
)
from app.logger import logger


class LoanService:
    def __init__(self):
        self.book_repo = BookRepository()
        self.user_repo = UserRepository()
        self.loan_repo = LoanRepository()

    def create_loan(self, db, data):
        book = self.book_repo.get_by_id(db, data.book_id)

        if not book:
            logger.warning(f"Intento de préstamo con libro inexistente: {data.book_id}")
            raise BookNotFoundError("El libro no existe.")

        user = self.user_repo.get_by_id(db, data.user_id)

        if not user:
            logger.warning(f"Intento de préstamo con usuario inexistente: {data.user_id}")
            raise UserNotFoundError("El usuario no existe.")

        if not book.disponible:
            logger.warning(f"Intento de préstamo de libro no disponible: {book.titulo}")
            raise BookNotAvailableError("El libro ya está prestado.")

        loan = self.loan_repo.create(db, data.user_id, data.book_id)

        book.disponible = False
        db.commit()
        db.refresh(book)

        logger.info(f"Préstamo creado correctamente. Libro: {book.titulo}, Usuario: {user.email}")

        return loan

    def return_loan(self, db, loan_id: int):
        loan = self.loan_repo.get_by_id(db, loan_id)

        if not loan:
            logger.warning(f"Intento de devolución con préstamo inexistente: {loan_id}")
            raise LoanNotFoundError("El préstamo no existe.")

        if loan.fecha_devolucion is not None:
            logger.warning(f"Intento de devolver préstamo ya cerrado: {loan_id}")
            raise LoanAlreadyReturnedError("Ese préstamo ya estaba cerrado.")

        loan.fecha_devolucion = datetime.utcnow()

        book = self.book_repo.get_by_id(db, loan.book_id)
        book.disponible = True

        db.commit()
        db.refresh(loan)

        logger.info(f"Préstamo devuelto correctamente: {loan_id}")

        return loan

    def get_user_history(self, db, user_id: int):
        user = self.user_repo.get_by_id(db, user_id)

        if not user:
            logger.warning(f"Consulta de historial con usuario inexistente: {user_id}")
            raise UserNotFoundError("El usuario no existe.")

        logger.info(f"Consultando historial del usuario: {user.email}")

        return self.loan_repo.get_by_user_id(db, user_id)
