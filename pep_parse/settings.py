import datetime as dt
from pathlib import Path

BASE_DIR = Path(__file__).parent
RESULTS_DIR = 'results'
DIR = BASE_DIR / RESULTS_DIR

DATETIME_FORMAT = '%Y-%m-%dT%H-%M-%S'
NOW_FORMATTED = dt.datetime.now().strftime(DATETIME_FORMAT)

HEADER_PEP = ('Статус', 'Количество')
FIELDS_NAME = ['number', 'name', 'status']
SUM_FILE_NAME = 'status_summary'
PEP_FILE_NAME = 'pep_%(time)s'
FILE_FORMAT = 'csv'
MODE_OPEN_FILE = 'w'
MODE_DOWNLOAD = 'wb'
CODE_PAGES = 'utf-8'

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']

ROBOTSTXT_OBEY = True

FEEDS = {
    RESULTS_DIR + '/' + PEP_FILE_NAME + '.' + FILE_FORMAT: {
        'format': FILE_FORMAT,
        'fields': FIELDS_NAME,
        'overwrite': True
    }
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
