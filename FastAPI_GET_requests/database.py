
# import basic libraries
import os
from dotenv import load_dotenv

# import parts from sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


load_dotenv()
user=os.getenv("USER")
password=os.getenv("PASSWORD")
database=os.getenv("DATABASE")

# database connection
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{user}:{password}@localhost:3306/{database}"

# create SQLalchemy engin
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Each instance of the SessionLocal class will be a database session. The class itself is not a database session yet.
# But once we create an instance of the SessionLocal class, this instance will be the actual database session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Now we will use the function declarative_base() that returns a class.
# Later we will inherit from this class to create each of the database models or classes (the ORM models)
Base = declarative_base()

