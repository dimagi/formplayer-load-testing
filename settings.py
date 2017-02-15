DOMAIN = ''
USERNAME = ''
PASSWORD = ''
DJANGO_HOST = 'http://localhost:8000'

APP_ID = ''

CASE_LIST_APP_ID = ''
CASE_LIST_SELECTIONS = []

CASE_DETAIL_APP_ID = ''
CASE_DETAIL_SELECTIONS = []

try:
    from localsettings import *
except ImportError:
    pass
