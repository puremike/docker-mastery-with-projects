# Use the official Node.js image as the base image
FROM node:22-slim

# Set the working directory inside the container
WORKDIR /app
WORKDIR /app/server

# Copy the server code to the working directory
COPY server .

# Install the server dependencies
RUN npm install

# Change to the client directory
WORKDIR /app
WORKDIR /app/client

# Copy the client code to the client directory
COPY client .

# Install the client dependencies
RUN npm --legacy-peer-deps install 

# Build the React application
RUN npm run build

# Change back to the app directory
WORKDIR /app/server

# Expose the port that the server listens on
EXPOSE 4000

# Run the Node.js server when the container starts
CMD [ "node", "server.js" ]

