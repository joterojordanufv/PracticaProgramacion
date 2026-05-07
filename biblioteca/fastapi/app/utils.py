def generate_books(books):
    for book in books:
        yield {
            "id": book.id,
            "titulo": book.titulo,
            "autor": book.autor,
            "genero": book.genero,
            "disponible": book.disponible
        }
