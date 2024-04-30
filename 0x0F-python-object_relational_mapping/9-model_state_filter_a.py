#!/usr/bin/python3
"""
Write a script that prints the first State object
from the database hbtn_0e_6_usa
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

states = session.query(State).filter(State.name.like("%a%")).order_by(State.id)

for row in states:
    print("{}: {}".format(row.id, row.name))

session.close()
