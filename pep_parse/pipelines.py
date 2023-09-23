import csv
import datetime as dt

from .settings import (BASE_DIR, RESULTS_DIR, DATETIME_FORMAT, FILE_FORMAT,
                       SUM_FILE_NAME, MODE_OPEN_FILE, CODE_PAGES, HEADER_PEP,
                       TOTAL)


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses = {}

    def process_item(self, item, spider):
        self.statuses[item['status']] = self.statuses.get(
            item['status'], 0) + 1
        return item

    def close_spider(self, spider):
        now_formatted = dt.datetime.now().strftime(DATETIME_FORMAT)
        file_name = f'{SUM_FILE_NAME}_{now_formatted}.{FILE_FORMAT}'
        results_dir = BASE_DIR / RESULTS_DIR
        results_dir.mkdir(exist_ok=True)
        file_path = results_dir / file_name
        with open(file_path, MODE_OPEN_FILE, encoding=CODE_PAGES) as file:
            csv.writer(
                file,
                dialect=csv.unix_dialect,
                quoting=csv.QUOTE_NONE
            ).writerows(
                [
                    HEADER_PEP,
                    *self.statuses.items(),
                    (TOTAL, sum(self.statuses.values()))
                ]
            )
