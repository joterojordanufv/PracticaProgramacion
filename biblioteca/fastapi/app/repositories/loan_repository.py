from sqlalchemy.orm import Session
from app.models.loan import Loan

class LoanRepository:
    def create(self, db: Session, user_id: int, book_id: int):
        loan = Loan(user_id=user_id, book_id=book_id)
        db.add(loan)
        db.commit()
        db.refresh(loan)
        return loan

    def get_by_id(self, db: Session, loan_id: int):
        return db.query(Loan).filter(Loan.id == loan_id).first()

    def get_by_user_id(self, db: Session, user_id: int):
        return db.query(Loan).filter(Loan.user_id == user_id).all()
