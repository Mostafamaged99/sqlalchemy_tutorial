import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
DB_URI = os.path.join(ROOT_DIR, 'database.db')
engine = create_engine(f'sqlite:///{DB_URI}', echo=True)

Base = declarative_base()

Base.metadata.create_all(bind = engine)