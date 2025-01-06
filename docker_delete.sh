#!/bin/bash

# Nom des conteneurs et images
REACT_CONTAINER="react-front"
FLASK_CONTAINER="flask-back"


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
