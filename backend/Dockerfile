# Étape 1 : Utilisation d'une image Python de base
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .

# Installer les dépendances depuis le fichier requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source de l'application Flask
COPY . .

# Exposer le port 5000 (port par défaut pour Flask)
EXPOSE 5000

# Commande pour démarrer l'application Flask
CMD ["python", "app.py"]
