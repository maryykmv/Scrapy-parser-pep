from collections import Counter
import csv
import datetime as dt

from .settings import (BASE_DIR, RESULTS_DIR, DATETIME_FORMAT, FILE_FORMAT,
                       SUM_FILE_NAME, MODE_OPEN_FILE, CODE_PAGES, HEADER_PEP)


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses = []

    def process_item(self, item, spider):
        self.statuses.append(item['status'])
        counter = Counter(self.statuses)
        self.results = [
            HEADER_PEP,
            *counter.items(),
        ]
        self.results.append(('Итого:', len(self.statuses)))
        return item

    def close_spider(self, spider):
        now_formatted = dt.datetime.now().strftime(DATETIME_FORMAT)
        file_name = f'{SUM_FILE_NAME}_{now_formatted}.{FILE_FORMAT}'
        file_path = BASE_DIR / RESULTS_DIR / file_name
        with open(file_path, MODE_OPEN_FILE, encoding=CODE_PAGES) as file:
            csv.writer(
                file,
                dialect=csv.unix_dialect,
                quoting=csv.QUOTE_NONE
            ).writerows(
                self.results
            )
