DOMAIN = ''
USERNAME = ''
PASSWORD = ''
DJANGO_HOST = 'http://localhost:8000'

APP_ID = ''

CASE_LIST_APP_ID = ''
CASE_LIST_SELECTIONS = []

CASE_DETAIL_APP_ID = ''
CASE_DETAIL_SELECTIONS = []

NIKSHAY_WORKFLOWS = {
    'manage_enrolment': [0],
    'tests': [2, 1],
    'adherence': [3],
    'task_list.treatment': [9, 0],
    'task_list.new_patient': [9, 1],
    'task_list.hiv': [9, 2],
    'task_list.test': [9, 3],
    'task_list.follow_up': [9, 4],
    'task_list.adherence': [9, 5],
    'referrals': [5, 3]
}

try:
    from localsettings import *
except ImportError:
    pass
