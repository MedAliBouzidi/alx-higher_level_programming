#!/usr/bin/python3
"""
     prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print('<Usage>: ./8-model_state_fetch_first.py\
            [mysql_username] [mysql_password] [database name]')
    else:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(sys.argv[1], sys.argv[2], sys.argv[3]))
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        first_instance = session.query(State).first()
        if first_instance is not None:
            print(f'{first_instance.id}: {first_instance.name}')
        else:
            print('Nothing')
