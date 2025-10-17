import csv
from logger_config import logger

from normaliz_path import normalaiz


def save_report(report_path: str, report: list[dict]):
    """Сохраняем отчет"""
    
    if not report_path:
        logger.warning("Нет пути для сохранения отчета")
        report_path = "reports/average-rating.csv"
    else:
        report_path = normalaiz(report_path)
        report_path = f"reports/{report_path}"



    try:
        with open(report_path, "w", newline='', encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["brand", "rating"])
            writer.writeheader()
            writer.writerows(report)
        logger.info(f"Отчет сохранен ✅: {report_path}")

    except Exception as e:
        logger.error(f"Не удалось сохранить отчет {report_path}: {e}")