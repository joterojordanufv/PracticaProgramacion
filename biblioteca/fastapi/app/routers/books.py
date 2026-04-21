from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.book import BookCreate, BookResponse
from app.services.book_service import BookService

router = APIRouter(prefix="/books", tags=["books"])
service = BookService()

@router.get("/", response_model=list[BookResponse])
def get_books(db: Session = Depends(get_db)):
    return service.get_all_books(db)

@router.post("/", response_model=BookResponse)
def create_book(data: BookCreate, db: Session = Depends(get_db)):
    try:
        return service.create_book(db, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/search", response_model=list[BookResponse])
def search_books(q: str, db: Session = Depends(get_db)):
    return service.search_books(db, q)
