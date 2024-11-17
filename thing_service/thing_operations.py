from random import uniform

from sqlalchemy.future import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from thing_service.thing_model import Base, Thing


class ThingDatabase:
    def __init__(self):
        self.engine = create_engine("postgresql://postgres:1234@localhost:5432/booking_info")
        Base.metadata.create_all(self.engine)

    def add_thing(self, thing):
        with sessionmaker(bind=self.engine)() as session:
            new_thing = Thing(thing_id=int(uniform(10000, 99999)), thing_name=thing)

            session.add(new_thing)
            session.commit()
            session.close()


    def get_thing(self, thing_id):
        with sessionmaker(bind=self.engine)() as session:
            thing = session.query(Thing).filter(thing_id=thing_id).first()

            return thing

    def get_things(self):
        with sessionmaker(bind=self.engine)() as session:
            things = session.query(Thing).all()

            return ([{"thing id": thing.thing_id,
                      "thing name": thing.thing_name} for thing in things])

    def delete_thing(self, thing_id):
        with sessionmaker(bind=self.engine) as session:
            thing = session.query(Thing).filter(thing_id=thing_id).delete()