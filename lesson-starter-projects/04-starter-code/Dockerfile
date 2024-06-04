## 1. Which base image do you want to use?
FROM openjdk:23-slim-bullseye

## 2. Set the working directory.
WORKDIR /app/src

## 3. Copy your source code file to the working directory.
COPY JavaApp.jar /app/src

## 4. Define the command to run when the container starts.

CMD [ "java", "-cp", "JavaApp.jar", "JavaApp" ]