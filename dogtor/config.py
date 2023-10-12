

"""aqui se puede declar mis configuraciones como una classe.
todas las configuraciones de mi aplicacion"""
import os
from dotenv import load_dotenv

load_dotenv()

class Confing:
    
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
    DB_NAME = os.getenv("DB_NAME")
    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
    )