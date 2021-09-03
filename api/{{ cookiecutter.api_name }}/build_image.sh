docker build -t worshop_image .

docker tag worshop_image gcr.io/static-smoke-324900/worshop_image

docker push gcr.io/static-smoke-324900/worshop_image