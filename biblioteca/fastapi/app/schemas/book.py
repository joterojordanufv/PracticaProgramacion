from pydantic import BaseModel

class BookCreate(BaseModel):
    titulo: str
    autor: str
    genero: str

class BookResponse(BaseModel):
    id: int
    titulo: str
    autor: str
    genero: str
    disponible: bool

    class Config:
        from_attributes = True
