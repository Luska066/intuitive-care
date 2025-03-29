import mysql.connector
from dotenv import load_dotenv
import os


class Mysql:

    def create(self):
        try:
            load_dotenv()
            db_config = {
                "host": os.getenv("MYSQL_HOST", "0.0.0.0"),
                "user": os.getenv("MYSQL_USER", "root"),
                "password": os.getenv("MYSQL_PASSWORD", "intuitive"),
                "database": os.getenv("MYSQL_DATABASE", "intuitive_db"),
                "port": int(os.getenv("MYSQL_PORT", 3306)),
            }
            conn = mysql.connector.connect(**db_config)
            if conn.is_connected():
                print("Conectado ao MySQL!")
                return conn
            else:
                print("Falha na conexão com o MySQL.")
        except mysql.connector.Error as err:
            print(f"Erro: {err}")
