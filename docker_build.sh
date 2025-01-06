#!/bin/bash

# Nom des images Docker (assurez-vous que les images ont été construites avec ces noms)
FRONTEND_IMAGE="react-front"
BACKEND_IMAGE="flask-back"

# Construire les images Docker (si ce n'est pas déjà fait)
echo "Building the frontend Docker image..."
docker build -t $FRONTEND_IMAGE ./frontend

echo "Building the backend Docker image..."
docker build -t $BACKEND_IMAGE ./backend

# Exécuter les conteneurs Docker
echo "Starting the backend container..."
docker run -d -p 5000:5000 --name backend $BACKEND_IMAGE

echo "Starting the frontend container..."
docker run -d -p 3000:3000 --name frontend $FRONTEND_IMAGE

echo "Containers are running:"
echo "Backend is running on http://localhost:5000"
echo "Frontend is running on http://localhost:3000"
