
from logger_config import logger
from collections import defaultdict


def aggregate_data(data: list[dict]) -> list[dict]:
    """Агрегируем бренды и считаем средний рейтинг"""

    if not data:
        logger.warning("Нет данных для агрегации")
        return []

    grouped = defaultdict(list)

    for row in data:
        grouped[row["brand"]].append(row)

    report = []

    for brand, items in grouped.items():
        ratings = [i["rating"] for i in items if isinstance(i["rating"], (float))]


        avg_rating = sum(ratings) / len(ratings) if ratings else 0

        
        report.append(
            {
            "brand": brand,
            "rating": round(avg_rating, 2),

            }
        )

    return report