# import datetime as dt

# from .constants import (BASE_DIR, RESULTS_DIR, FILE_FORMAT,
#                         FIELDS_NAME, PEP_FILE_NAME, DATETIME_FORMAT)

from .constants import (FILE_FORMAT, FIELDS_NAME)

BOT_NAME = 'pep_parse'
# DIR = str(BASE_DIR / RESULTS_DIR)
# NOW_FORMATTED = dt.datetime.now().strftime(DATETIME_FORMAT)


SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

FEEDS = {
    'results/pep_%(time)s.' + FILE_FORMAT: {
        'format': FILE_FORMAT,
        'fields': FIELDS_NAME,
        'overwrite': True
    }
}

# если делать через константы падает тест
#  FAILED tests/test_settings.py::test_settings_feeds - AssertionError: 
# Убедитесь, что в ключе словаря `FEEDS` перед именем файла 
# указан путь к директории `results/`
# FEEDS = {
#     DIR + '/' + PEP_FILE_NAME + str(NOW_FORMATTED) + '.' + FILE_FORMAT: {
#         'format': FILE_FORMAT,
#         'fields': FIELDS_NAME,
#         'overwrite': True
#     }
# }

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
