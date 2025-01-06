#!/bin/bash

# Set script to exit immediately if any command fails
set -e

# Paths to the Kubernetes configuration files
CLIENT_PATH="./k8s"

# Delete existing Kubernetes resources for the server and client
echo "Deleting existing Kubernetes resources (if they exist)..."
kubectl delete -f "$CLIENT_PATH" --ignore-not-found

# Apply new configurations to create/recreate Kubernetes resources
echo "Applying Kubernetes configurations..."
kubectl apply -f "$CLIENT_PATH"

echo "Kubernetes deployment completed successfully."