from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, Boolean
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
        return f"Player id: {self.id}: " \
            + f"Player name:{self.name}, " \
            + f"{self.email}"\
            + f"Score:{self.point}"
    
    questions = relationship ("Question", secondary="player_quiz", backref="players")
    quizzes = relationship ("Quiz", backref="players")
    

class Question (Base):
    __tablename__= 'questions'
    id = Column(Integer(), primary_key=True)
    question= Column(String())
    answer=Column (String())
    def __repr__(self):
        return f"Question id:{self.id}: " \
            + f"Question:{self.question} " \
            + f"Answer:{self.answer}"
    
    players = relationship ("Player", secondary="player_quiz", backref="Question")
    quizzes = relationship ("Quiz", backref="Question")

class Quiz (Base):
    __tablename__='quizzes'
    id = Column(Integer(), primary_key=True)
    question_id = Column(Integer(), ForeignKey ("questions.id"))
    player_id =Column(Integer(), ForeignKey ("players.id"))
    correct_answer= Column (Boolean, nullable=(False))
    def __repr__(self):
        return f"Quiz {self.id}: " \
            + f"Question id {self.question_id}"\
            + f"Player id{self.player_id}"\
            + f"Answered Correctly{self.correct_answer}"

    