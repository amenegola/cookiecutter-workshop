docker build -t workshop_image .

docker tag workshop_image gcr.io/static-smoke-324900/workshop_image

docker push gcr.io/static-smoke-324900/workshop_image