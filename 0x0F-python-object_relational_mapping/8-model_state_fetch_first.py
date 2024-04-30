#!/usr/bin/python3
"""
Write a script that lists all State objects
from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv

if len(argv) != 4:
    print("Use: username, database name, password")
    exit(1)

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

state = session.query(State).order_by(State.id).first()

if state is None:
    print('Nothing')
print(f"{state.id}: {state.name}")
session.close()
