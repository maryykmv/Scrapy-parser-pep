from pathlib import Path

BASE_DIR = Path(__file__).parent
RESULTS_DIR = 'results'

DATETIME_FORMAT = '%Y-%m-%dT%H-%M-%S'

HEADER_PEP = ('Статус', 'Количество')
FIELDS_NAME = ['number', 'name', 'status']
SUM_FILE_NAME = 'status_summary'
PEP_FILE_NAME = 'pep_'
FILE_FORMAT = 'csv'
MODE_OPEN_FILE = 'w'
MODE_DOWNLOAD = 'wb'
CODE_PAGES = 'utf-8'
