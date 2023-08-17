from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

player_quiz=Table (
    "player_quiz",
    Base.metadata,
    Column ("id", Integer, primary_key=True),
    Column ("player_id", ForeignKey("players.id")),
    Column ("quiz_id", ForeignKey("quizzes.id"))
)

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
    
class Question (Base):
    __tablename__= 'questions'
    id = Column(Integer(), primary_key=True)
    question= Column(String())
    answer=Column (String())
    def __repr__(self):
        return f"Question {self.id}: " \
            + f"{self.question} " \
            + f"{self.answer}"
        
class Quiz (Base):
    __tablename__='quizzes'
    id = Column(Integer(), primary_key=True)
    question_id = Column(Integer(), ForeignKey ("questions.id"))
    def __repr__(self):
        return f"Quiz {self.id}: " \
            + f"{self.question_id}"