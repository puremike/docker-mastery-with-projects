# Use the official Node.js image as the base image
FROM node:22-slim

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json .

# Install the dependencies
RUN npm install

# Copy the other source code into the working directory
COPY . .

# Expose the port that the API listens on
EXPOSE 3001

# Run the Node.js application when the container starts
CMD [ "node", "index.js" ]