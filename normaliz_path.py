
from logger_config import logger

def normalaiz(path: str) -> str:
    """Проверка и нормализация имени файла/пути"""
    
    if not path.strip().endswith(".csv"):
        logger.info("Нормализация имени файла")
        path = f"{path}.csv"

    return path