from app.repositories.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.repo = UserRepository()

    def get_all_users(self, db):
        return self.repo.get_all(db)

    def create_user(self, db, data):
        if not data.nombre.strip() or not data.email.strip():
            raise ValueError("Nombre y email son obligatorios.")

        existing = self.repo.get_by_email(db, data.email)
        if existing:
            raise ValueError("Ese email ya está registrado.")

        return self.repo.create(db, data.nombre, data.email)
