DOMAIN = ''
USERNAME = ''
PASSWORD = ''
DJANGO_HOST = 'http://localhost:8000'

try:
    from localsettings import *
except ImportError:
    pass
