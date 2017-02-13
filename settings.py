import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_DIR = os.path.join(BASEDIR, 'tsung', 'templates')
BUILD_DIR = os.path.join(BASEDIR, 'tsung', 'build')

TSUNG_DTD_PATH = '/usr/local/src/tsung/tsung-1.0.dtd'
FORMPLAYER_HOST = 'localhost'
FORMPLAYER_PORT = 8080

DOMAIN = 'domain'
try:
    from localsettings import *
except ImportError:
    pass
