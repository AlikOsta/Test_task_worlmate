import csv
from logger_config import logger

from normaliz_path import normalaiz


def read_csv(link_list: list) -> list[dict]:
    """Чтение CSV файлов и формируем единые данные."""

    data = []

    if not link_list:
        logger.warning("Нет путей для чтения файлов")
        return data

    for csv_path in link_list:
        csv_path = normalaiz(csv_path)
        
        try:
            with open(csv_path, newline='', encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    brand = row.get("brand", "").strip().lower()
                    rating_str = row.get("rating", "").strip().replace(",", ".")


                    rating = float(rating_str) if rating_str else None


                    data.append(
                        {
                            "brand": brand,
                            "rating": rating,

                        }
                    )

        except Exception as e:
            logger.error(f"Не смог прочитать файл - {csv_path} - {e}")
            continue

    return data