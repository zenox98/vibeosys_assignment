from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

USERNAME = 'zen'
PASSWORD = 'vibeosys1234'
HOST = 'localhost'
PORT = '3306'
DATABASE = 'vibeosys'

URL_DATABASE = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

engine = create_engine(URL_DATABASE, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
