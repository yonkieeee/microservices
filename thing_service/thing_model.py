from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import BIGINT
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Thing(Base):
    __tablename__ = 'things'

    thing_id = Column(BIGINT,primary_key=True, nullable=False)
    thing_name = Column(String(55))