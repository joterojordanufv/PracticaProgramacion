from app.repositories.book_repository import BookRepository

class BookService:
    def __init__(self):
        self.repo = BookRepository()

    def get_all_books(self, db):
        return self.repo.get_all(db)

    def create_book(self, db, data):
        if not data.titulo.strip() or not data.autor.strip() or not data.genero.strip():
            raise ValueError("Todos los campos son obligatorios.")
        return self.repo.create(db, data.titulo, data.autor, data.genero)

    def search_books(self, db, q):
        return self.repo.search(db, q)
