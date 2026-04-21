from sqlalchemy import Column, Integer, String, Boolean

from app.database import Base

class Book(Base):

    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)

    titulo = Column(String, nullable=False)

    autor = Column(String, nullable=False)

    genero = Column(String, nullable=False)

    disponible = Column(Boolean, default=True)

    @property

    def estado(self):

        return "Disponible" if self.disponible else "Prestado"
