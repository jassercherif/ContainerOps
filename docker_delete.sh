#!/bin/bash

# Nom des conteneurs et images
REACT_CONTAINER="jassercherif/react-front:v0.0."
FLASK_CONTAINER="jassercherif/flask-back:v0.0."


# Supprimer les conteneurs s'ils existent
echo "Arrêt et suppression des conteneurs si existants..."

# Arrêter les conteneurs
docker stop $REACT_CONTAINER $FLASK_CONTAINER 2>/dev/null

# Supprimer les conteneurs
docker rm $REACT_CONTAINER $FLASK_CONTAINER 2>/dev/null

# Supprimer les images Docker si elles existent
echo "Suppression des images si existantes..."

docker rmi $REACT_CONTAINER $FLASK_CONTAINER 2>/dev/null

echo "Nettoyage terminé."