## Base Image
FROM node:lts-alpine3.20

## Working Directory
WORKDIR /app/

## Copy Source code
COPY package*.json .

## Install Dependencies
RUN npm install

# Copy the files into the working directory
COPY . .

## Expose container port
EXPOSE 3000

## Commands to execute application
CMD [ "node", "app.js" ]