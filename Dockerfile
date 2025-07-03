# Base image with Python and Node.js
FROM --platform=linux/amd64 python:3.8-slim

# Install Node.js and npm
RUN apt-get update && apt-get install -y nodejs npm \
    && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/*

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements files
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Install React dependencies
WORKDIR /app/src/frontend
RUN npm install

# Build React app
RUN npm run build

# Set working directory back to root
WORKDIR /app

# Expose ports for services
EXPOSE 3000 5005 7474 7687 8000

# Start services using docker-compose
CMD ["/bin/bash", "./scripts/start-services.sh"]