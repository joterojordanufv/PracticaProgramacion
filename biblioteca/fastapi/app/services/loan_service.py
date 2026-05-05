from datetime import datetime
from app.repositories.book_repository import BookRepository
from app.repositories.user_repository import UserRepository
from app.repositories.loan_repository import LoanRepository

class LoanService:
    def __init__(self):
        self.book_repo = BookRepository()
        self.user_repo = UserRepository()
        self.loan_repo = LoanRepository()

    def create_loan(self, db, data):
        book = self.book_repo.get_by_id(db, data.book_id)
        if not book:
            raise ValueError("El libro no existe.")

        user = self.user_repo.get_by_id(db, data.user_id)
        if not user:
            raise ValueError("El usuario no existe.")

        if not book.disponible:
            raise ValueError("El libro ya está prestado.")

        loan = self.loan_repo.create(db, data.user_id, data.book_id)
        book.disponible = False
        db.commit()
        db.refresh(book)
        return loan

    def return_loan(self, db, loan_id: int):
        loan = self.loan_repo.get_by_id(db, loan_id)
        if not loan:
            raise ValueError("El préstamo no existe.")

        if loan.fecha_devolucion is not None:
            raise ValueError("Ese préstamo ya estaba cerrado.")

        loan.fecha_devolucion = datetime.utcnow()
        book = self.book_repo.get_by_id(db, loan.book_id)
        book.disponible = True

        db.commit()
        db.refresh(loan)
        return loan

    def get_user_history(self, db, user_id: int):
        user = self.user_repo.get_by_id(db, user_id)
        if not user:
            raise ValueError("El usuario no existe.")
        return self.loan_repo.get_by_user_id(db, user_id)
