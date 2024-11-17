from random import uniform
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from user_service.user_model import Base, User


class UserDatabase:
    def __init__(self):
        self.engine = create_engine("postgresql://postgres:1234@localhost:5432/booking_info")
        Base.metadata.create_all(self.engine)

    def add_user(self, user_name, user_surname):
        with sessionmaker(bind=self.engine)() as session:
            new_thing = User(user_id=int(uniform(10000, 99999)),
                             user_name=user_name,
                             user_surname=user_surname
                             )

            session.add(new_thing)
            session.commit()
            session.close()


    def get_user(self, user_id):
        with sessionmaker(bind=self.engine)() as session:
            user = session.query(User).filter(User.user_id == user_id).first()

            return user

    def get_users(self):
        with sessionmaker(bind=self.engine)() as session:
            users = session.query(User).all()

            return ([{"user id": user.user_id,
                     "user name": user.user_name,
                     "user surname": user.user_surname}for user in users])



    def delete_user(self, user_id):
        with sessionmaker(bind=self.engine) as session:
            thing = session.query(User).filter(User.user_id == user_id).delete()