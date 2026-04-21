from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models.book import Book

class BookRepository:
    def get_all(self, db: Session):
        return db.query(Book).all()

    def create(self, db: Session, titulo: str, autor: str, genero: str):
        book = Book(titulo=titulo, autor=autor, genero=genero, disponible=True)
        db.add(book)
        db.commit()
        db.refresh(book)
        return book

    def get_by_id(self, db: Session, book_id: int):
        return db.query(Book).filter(Book.id == book_id).first()

    def search(self, db: Session, q: str):
        return db.query(Book).filter(
            or_(
                Book.titulo.ilike(f"%{q}%"),
                Book.autor.ilike(f"%{q}%")
            )
        ).all()
