from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

load_dotenv()
db_config = {
    "host": os.getenv("MYSQL_HOST", "0.0.0.0"),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", "intuitive"),
    "database": os.getenv("MYSQL_DATABASE", "intuitive_db"),
    "port": os.getenv("MYSQL_PORT", 3306),
}

DATABASE_URL = ("mysql+mysqlconnector://"
                + db_config.get("user") +
                ":" + db_config.get("password") +
                "@" + db_config.get("host")
                + ":" + db_config.get("port")
                + "/" + db_config.get("database"))

engine = create_engine(DATABASE_URL)
SESSION = sessionmaker(autocommit=False, autoflush=False, bind=engine)
BASE = declarative_base()
