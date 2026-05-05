from sqlalchemy.orm import Session
from app.models.user import User

class UserRepository:
    def get_all(self, db: Session):
        return db.query(User).all()

    def get_by_id(self, db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    def get_by_email(self, db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    def create(self, db: Session, nombre: str, email: str):
        user = User(nombre=nombre, email=email)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
