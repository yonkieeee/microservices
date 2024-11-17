from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import BIGINT
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    user_id = Column(BIGINT,primary_key=True, nullable=False)
    user_name = Column(String(50))
    user_surname = Column(String(50))
