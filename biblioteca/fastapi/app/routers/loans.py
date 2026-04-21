from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.loan import LoanCreate, LoanResponse
from app.services.loan_service import LoanService

router = APIRouter(prefix="/loans", tags=["loans"])
service = LoanService()

@router.post("/", response_model=LoanResponse)
def create_loan(data: LoanCreate, db: Session = Depends(get_db)):
    try:
        return service.create_loan(db, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.patch("/{loan_id}/return", response_model=LoanResponse)
def return_loan(loan_id: int, db: Session = Depends(get_db)):
    try:
        return service.return_loan(db, loan_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/user/{user_id}")
def user_history(user_id: int, db: Session = Depends(get_db)):
    try:
        loans = service.get_user_history(db, user_id)
        return [
            {
                "id": loan.id,
                "book_id": loan.book_id,
                "user_id": loan.user_id,
                "titulo": loan.book.titulo,
                "fecha_prestamo": loan.fecha_prestamo,
                "fecha_devolucion": loan.fecha_devolucion,
                "activo": loan.fecha_devolucion is None
            }
            for loan in loans
        ]
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
