# Utilisation de l'image officielle Python 3.9 slim comme image de base
FROM python:3.9-slim

# Définition du répertoire de travail à /app

# Copie le fichier des dépendances dans le répertoire de travail
COPY requirements.txt .

# Installation des dépendances Python spécifiées dans requirements.txt
RUN pip install -r requirements.txt
RUN pip install uvicorn

# Copie le code de l'application dans le répertoire de travail
COPY . .

# Expose le port 8000 pour l'application web
EXPOSE 8000

# Définition de la variable d'environnement pour l'URL de la base de données
ENV DATABASE_URL=mysql+pymysql://root:@localhost:3307/todosdb

# Définition du répertoire de travail et exécution de la commande pour démarrer l'application web
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]