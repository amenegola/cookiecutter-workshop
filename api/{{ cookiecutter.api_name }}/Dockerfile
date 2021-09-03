FROM python:3.7

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /source
ADD . /source/

EXPOSE 8080

CMD ["gunicorn","--bind","0.0.0.0:8080","-w","6","-k","uvicorn.workers.UvicornWorker","run:app"]