FROM python:3.7

WORKDIR /source
ADD . /source/

RUN pip install --upgrade pip
RUN pip install -r /source/requirements.txt

EXPOSE 8080

CMD ["gunicorn","--bind","0.0.0.0:8080","-w","6","-k","uvicorn.workers.UvicornWorker","run:app"]