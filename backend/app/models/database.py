# Import library yang dibutuhkan
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.engine import Engine
from .base import Base


# Inisiasi Database Engine
print("Connecting to database...")
engine: Engine | None = None

try:
  engine = create_engine("mysql+pymysql://admin:121995@localhost:3306/pt_stdu", echo=True)
  Base.metadata.create_all(engine)
  print("Connected to database!")
  
except Exception as error:
  print(f"Failed to connect to database. Error message: {error}")


# Buat sesi database, untuk memudahkan eksekusi query
print("Creating database session...")
session: Session = Session()

try:
  Session = sessionmaker(bind=engine)
  session = Session()
  print("Database session created!")
  
except Exception as error:
  print(f"Failed to create session. Error message: {error}")
