from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    fecha_prestamo = Column(DateTime, default=datetime.utcnow)
    fecha_devolucion = Column(DateTime, nullable=True)

    user = relationship("User")
    book = relationship("Book")

    @property
    def activo(self):
        return self.fecha_devolucion is None
