import os
from dotenv import load_dotenv
from fastapi import FastAPI
from app.controller import app
import uvicorn

load_dotenv()
app_env = os.getenv('OS_ENV')

if __name__ == '__main__':
    _logger.debug('application instance created')
    uvicorn.run(app, host='0.0.0.0', port=8080, log_level='debug')
