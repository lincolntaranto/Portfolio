from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

db_url = os.getenv("DATABASE_URL")

if not db_url:
    raise "DATABASE_URL não encontrada."

db = create_engine(db_url)

Base = declarative_base()

