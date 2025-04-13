import psycopg2
from psycopg2 import OperationalError
from dotenv import load_dotenv
import os

# Carrega as variáveis do .env
load_dotenv()

def create_connection():
    try:
        connection = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        print("✅ Conexão com o banco de dados estabelecida com sucesso.")
        return connection
    except OperationalError as e:
        print(f"❌ Erro ao conectar com o banco de dados: {e}")
        return None
