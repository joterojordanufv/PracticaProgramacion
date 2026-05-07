from app.repositories.user_repository import UserRepository
from app.exceptions.custom_exceptions import DuplicateEmailError
from app.logger import logger


class UserService:
    def __init__(self):
        self.repo = UserRepository()

    def get_all_users(self, db):
        logger.info("Consultando listado de usuarios")
        return self.repo.get_all(db)

    def create_user(self, db, data):
        if not data.nombre.strip() or not data.email.strip():
            logger.warning("Intento de crear usuario con campos vacíos")
            raise ValueError("Nombre y email son obligatorios.")

        existing = self.repo.get_by_email(db, data.email)

        if existing:
            logger.warning(f"Intento de registrar email duplicado: {data.email}")
            raise DuplicateEmailError("Ese email ya está registrado.")

        user = self.repo.create(db, data.nombre, data.email)
        logger.info(f"Usuario creado correctamente: {user.email}")
        return user
