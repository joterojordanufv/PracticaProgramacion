from functools import wraps
from app.logger import logger


def log_action(action_name: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.info(f"Iniciando acción: {action_name}")
            result = func(*args, **kwargs)
            logger.info(f"Acción completada: {action_name}")
            return result
        return wrapper
    return decorator
