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
quiz_question =Table(
    "quiz_question",
    Base.metadata,
    Column ("id", Integer, primary_key=True),
    Column ("quiz_id", ForeignKey("quizzes.id")),
    Column ("question_id", ForeignKey("questions.id"))
)
track_answer =Table(
    "player_question_track",
    Base.metadata,
    Column ("id", Integer, primary_key=True),
    Column ("player_id", ForeignKey("players.id")),
    Column ("question_id", ForeignKey("questions.id")),
    Column ("points", String())
)


class Player(Base):
    __tablename__='players'
 
    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name=Column(String())
    username= Column(String())

    def __init__ (self,first_name, last_name,username):
        self.first_name=first_name
        self.last_name=last_name
        self.username=username

    def __repr__(self):
        return f"Player id: {self.id}: " \
            + f"Player first name:{self.first_name}, " \
            + f"Player last name:{self.last_name}"\
            + f"username:{self.username}"

    questions=relationship("Question", secondary=track_answer, back_populates="players")


#Add new player  

    @classmethod
    def new_player(cls, first_name, last_name, username):
        add_player = cls(first_name=first_name, last_name=last_name, username=username)
    
        session.add(add_player)
        session.commit()
        return add_player

class Question (Base):
    __tablename__= 'questions'
    id = Column(Integer(), primary_key=True)
    question= Column(String())
    answer=Column (String())
    point=Column(Integer())

    def __init__ (self,question, answer,point):
        self.question=question
        self.answer=answer
        self.point=point

    def correct_answer (self, answer):
        return self.answer ==answer


    def __repr__(self):
        return f"Question id:{self.id}: "\
            + f"Question:{self.question} "\
            + f"Answer:{self.answer}"\
            + f"Point:{self.point}"
    
    players=relationship("Player", secondary=track_answer, back_populates="questions")
    quizzes=relationship("Quiz", secondary=quiz_question , back_populates="questions")
      

    
    @classmethod
    def get_questions (cls, question):
        cls.all.append(question)
    

class Quiz (Base):
    __tablename__='quizzes'
    id = Column(Integer(), primary_key=True)
    player_id =Column(Integer(), ForeignKey ("players.id"))

    def __init__ (self,player_id):
        self.player_id=player_id
    
              
    def __repr__(self):
        return f"Quiz {self.id}: " \
            + f"Player id{self.player_id}"

    questions=relationship("Question", secondary=quiz_question , back_populates="quizzes")




