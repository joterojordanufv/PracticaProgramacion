from pydantic import BaseModel
from datetime import datetime

class LoanCreate(BaseModel):
    user_id: int
    book_id: int

class LoanResponse(BaseModel):
    id: int
    user_id: int
    book_id: int
    fecha_prestamo: datetime
    fecha_devolucion: datetime | None

    class Config:
        from_attributes = True
