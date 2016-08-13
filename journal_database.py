import sys
from sqlalchemy import Column, String, Date, Integer

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Journal(Base):
	__tablename__ = 'journal'
	id = Column(Integer, primary_key=True)
	date = Column(Date, nullable=False)
	post = Column(String,nullable=False)

engine = create_engine('sqlite:///journal.db')
Base.metadata.create_all(engine)