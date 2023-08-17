from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, Boolean, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

engine = create_engine ('sqlite:///studying-VScode-shortcut-quiz.db')
Session = sessionmaker(bind=engine)
session = Session()

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

    #Add new player  
    def add_player (name,email, point):
        add_player=Player (
            full_name = name,
            email=email,
            point =f'{point}'
        )
        session.add(add_player)
        session.commit ()

    #Delete player and count how many player left
    def remove_player (name):
        remove_player=session.query (Player).filter(Player.name).count ()
        session.delete(remove_player)
        session.commit()

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

    def add_question (question,answer):
        question=Question (
            question = question,
            answer=answer
        )
        session.add(question)
        session.commit ()

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
    
 
    