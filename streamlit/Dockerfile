# Utiliser une image de base Python
FROM python:3.8-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers requirements.txt dans le conteneur
COPY requirements.txt .env ./

# Installer les dépendances
RUN pip install -r requirements.txt

# Copier les fichiers de l'application dans le conteneur
COPY . .

# Exposer le port utilisé par Streamlit
EXPOSE 8501

# Exécuter l'application Streamlit
CMD ["streamlit", "run", "app.py"]