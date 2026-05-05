from pydantic import BaseModel

class UserCreate(BaseModel):
    nombre: str
    email: str

class UserResponse(BaseModel):
    id: int
    nombre: str
    email: str

    class Config:
        from_attributes = True
