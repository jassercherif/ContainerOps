#!/bin/bash

# Define image versions
SERVER_IMAGE="jassercherif/flask-back:v0.0"
CLIENT_IMAGE="jassercherif/react-front:v0.0"

echo "Starting build and push process..."

# Build and push server image
echo "Building server image..."
cd backend || exit 1
docker build -t $SERVER_IMAGE .
if [ $? -ne 0 ]; then
  echo "Server image build failed"
  exit 1
fi

echo "Pushing server image to Docker Hub..."
docker push $SERVER_IMAGE
if [ $? -ne 0 ]; then
  echo "Server image push failed"
  exit 1
fi
cd ..

# Build and push client image
echo "Building client image..."
cd frontend || exit 1
docker build -t $CLIENT_IMAGE .
if [ $? -ne 0 ]; then
  echo "Client image build failed"
  exit 1
fi

echo "Pushing client image to Docker Hub..."
docker push $CLIENT_IMAGE
if [ $? -ne 0 ]; then
  echo "Client image push failed"
  exit 1
fi
cd ..

echo "Build and push process completed successfully!"