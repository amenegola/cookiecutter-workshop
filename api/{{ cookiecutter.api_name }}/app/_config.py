import logging
from logging.handlers import TimedRotatingFileHandler
import graypy
import pathlib
import os
import sys
from dotenv import load_dotenv

load_dotenv()
app_env = os.getenv('OS_ENV')
graylog_url = os.getenv('GRAYLOG_URL')
graylog_port = 12201
application_name = os.getenv('APP_NAME')

PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent.parent

with open(PACKAGE_ROOT / 'VERSION') as version_file:
    __version__ = version_file.read().strip()


FORMATTER = logging.Formatter(
    "%(project)s - %(levelname)s - %(app_version)s - %(application_name)s - "
    "%(app_env)s -  %(asctime)s — %(name)s"
    "%(funcName)s:%(lineno)d — %(message)s"
)

if app_env == 'local':
    logging.basicConfig(filename='logs/ml_api.log',
                        filemode='a')
    LOG_DIR = PACKAGE_ROOT / 'logs'
    LOG_DIR.mkdir(exist_ok=True)
    LOG_FILE = LOG_DIR / 'ml_api.log'

class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = ''
    SERVER_PORT = 8080


class ProductionConfig(Config):
    DEBUG = False
    SERVER_ADDRESS: os.environ.get('SERVER_ADDRESS', '0.0.0.0')
    SERVER_PORT: os.environ.get('SERVER_PORT', '8080')


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_file_handler():
    file_handler = TimedRotatingFileHandler(
        LOG_FILE, when='midnight')
    file_handler.setFormatter(FORMATTER)
    return file_handler

def get_graylog_handler():
    handler = graypy.GELFUDPHandler(graylog_url, graylog_port)

    return handler

def get_logger(*, logger_name):
    """Get logger with prepared handlers."""

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    logger.propagate = True

    #local dev logging handlers
    if app_env == 'local':
        logger.addHandler(get_console_handler())
        logger.addHandler(get_file_handler())

    #prd/desenv/develop logging handler
    else:
        logger.addHandler(get_graylog_handler())

    logger = logging.LoggerAdapter(logger)

    return logger
