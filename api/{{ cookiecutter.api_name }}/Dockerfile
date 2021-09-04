FROM python:3.7

ADD . /source/
WORKDIR /source

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["gunicorn","--bind","0.0.0.0:8080","-w","6","-k","uvicorn.workers.UvicornWorker","app.controller:app"]