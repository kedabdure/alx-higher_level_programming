#!/usr/bin/python3
"""
Write a script that lists all State objects
that contain the letter a from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if len(argv) != 4:
    print('use: username, password, database name')
    exit(1)

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

states = session.query(State).where(State.id == 2)\
            .update({'name': 'New Mexico'})
session.commit()
session.close()
