DOMAIN = ''
USERNAME = ''
PASSWORD = ''
DJANGO_URI = 'http://localhost:8000'
DJANGO_HOST = 'localhost:8000'
RESTORE_AS = None

APP_ID = ''

CASE_LIST_SELECTIONS = []

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

NIKSHAY_DOMAIN = 'enikshay'
NIKSHAY_APP_ID = '2c07583502c70fc7fa29bf138215b47e'

try:
    from localsettings import *
except ImportError:
    pass
