docker build -t worshop_image:1.0 .

docker tag workshop-python gcr.io/static-smoke-324900/workshop-python

docker push gcr.io/static-smoke-324900/workshop-python:1.0