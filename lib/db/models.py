from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class Player(Base):
    __tablename__='players'
 
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    email=Column(String, unique=True)
    point= Column(String())
    def __repr__(self):
        return f"Player {self.id}: " \
            + f"{self.name}, " \
            + f"{self.email}"\
            + f"{self.point}"