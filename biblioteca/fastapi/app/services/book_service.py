from app.repositories.book_repository import BookRepository
from app.logger import logger
from app.decorators import log_action


class BookService:
    def __init__(self):
        self.repo = BookRepository()

    def get_all_books(self, db):
        logger.info("Consultando catálogo completo de libros")
        return self.repo.get_all(db)

    @log_action("crear libro")
    def create_book(self, db, data):
        if not data.titulo.strip() or not data.autor.strip() or not data.genero.strip():
            logger.warning("Intento de crear libro con campos vacíos")
            raise ValueError("Todos los campos son obligatorios.")

        book = self.repo.create(db, data.titulo, data.autor, data.genero)
        logger.info(f"Libro creado correctamente: {book.titulo}")
        return book

    def search_books(self, db, q):
        logger.info(f"Búsqueda de libros por título o autor: {q}")
        return self.repo.search(db, q)
