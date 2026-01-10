from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv() 

connection_string = os.getenv("CONNECTION_STRING")
engine = create_engine(connection_string, echo=True)

session_local = sessionmaker(bind=engine)

def get_session():
    db_session = session_local()
    try:
        yield db_session
        db_session.commit()
    except:
        db_session.rollback()
        raise
    finally:
        db_session.close()