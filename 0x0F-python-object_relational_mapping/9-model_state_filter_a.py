#!/usr/bin/python3
"""
    lists all State objects that contain
    the letter a from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print('<Usage>: ./9-model_state_filter_a.py\
            [mysql_username] [mysql_password] [database name]')
    else:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(sys.argv[1], sys.argv[2], sys.argv[3]))
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        instances = session.query(State).filter(State.name.like('%a%')) \
            .order_by(State.id)
        for instance in instances:
            print(f'{instance.id}: {instance.name}')
