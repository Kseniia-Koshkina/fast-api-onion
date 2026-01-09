from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from db.base_model import Base 

load_dotenv() 

connection_string = os.getenv("CONNECTION_STRING")
engine = create_engine(connection_string, echo=True)

database_session = sessionmaker(bind=engine)