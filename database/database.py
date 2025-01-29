import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def connect_to_database():
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        print("Connexion à la base de données réussie !")
        db.close()
    except Exception as e:
        print(f"Erreur de connexion à la base de données : {e}")

def close_database():
    """Ferme la connexion à la base de données."""
    try:
        engine.dispose()
        print("Connexion fermée avec succès.")
    except Exception as e:
        print(f"Erreur lors de la fermeture de la connexion : {e}")