## Base Image
FROM python:3.8-slim

## Work Directory
WORKDIR /app/

## Install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

## Copy source code
COPY . .

## Expose container port
EXPOSE 5001

## Execute Application
CMD [ "python", "app.py" ]

## This docker command without setting the ENV in Dockerfile will look like: 
## docker run --rm -p 5001:5001 --network grade-server -e GRADE_SERVICE_HOST=node-app_container-name --name flask-app-api flask-api

## To create a network to run both containers:
## docker network create grade-server
