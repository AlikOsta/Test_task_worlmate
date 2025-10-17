
from read_csv import read_csv
from aggregate_data import aggregate_data
from save_report import save_report
from tabulate import tabulate

from config_argparse import args
from logger_config import logger



def main():
    data = read_csv(args.files)

    if data:
        report = aggregate_data(data)
        save_report(args.report, report)

        print(tabulate(report, headers="keys", tablefmt="grid"))
    else:
        logger.warning("Отчет не может быть сформирован")



if __name__ == "__main__":
    logger.info("✅ Запуск скрипта ✅")

    main()