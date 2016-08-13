from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date

from journal_database import Journal, Base
engine = create_engine('sqlite:///journal.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

date1 = date.today()
entry1 = Journal(date=date1,post="When I was a kid all i wanted to do was code.\nThen I gave up because I hated front end development!:(")
session.add(entry1)
session.commit()


