import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de la base de données
DATABASE_URL = os.getenv('DATABASE_URL', "mysql+pymysql://root:@localhost:3306/todosdb")

# Créer un moteur de bdd pour la connexion
engine = create_engine(DATABASE_URL)

# Créer une session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Fonction pour obtenir une session de base de données
def get_db():
    db = SessionLocal()
    try:
        # La session de base de données est ouverte et est utilisée dans la requête
        yield db
    finally:
        # Fermeture de la session de base de données a la fin de la requete
        db.close()