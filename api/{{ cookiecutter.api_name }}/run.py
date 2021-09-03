import os
from dotenv import load_dotenv
from fastapi import FastAPI
from api.controller import app
from api.config import get_logger
import uvicorn

load_dotenv()
app_env = os.getenv('OS_ENV')
_logger = get_logger(logger_name=__name__)

if __name__ == '__main__':
    _logger.debug('application instance created')
    uvicorn.run(app, host='0.0.0.0', port=8080, log_level='debug')
