#!/usr/bin/python3
"""
    changes the name of a State object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print('<Usage>: ./12-model_state_update_id_2.py\
            [mysql_username] [mysql_password] [database name]')
    else:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(sys.argv[1], sys.argv[2], sys.argv[3]))
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        to_update = session.query(State).filter_by(id=2).first()
        to_update.name = "New Mexico"
        session.add(to_update)
        session.commit()
