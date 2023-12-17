#!/usr/bin/python3
"""
    adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print('<Usage>: ./11-model_state_insert.py\
            [mysql_username] [mysql_password] [database name]')
    else:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(sys.argv[1], sys.argv[2], sys.argv[3]))
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(State(name="Louisiana"))
        new_instance = session.query(State).filter_by(name="Louisiana").first()
        print(new_instance.id)
        session.commit()
