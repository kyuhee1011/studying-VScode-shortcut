from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, Boolean, MetaData
from sqlalchemy.ext.declarative import declarative_base
from helpers.prompt import Prompt
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
    def __repr__(self):
        return f"Player id: {self.id}: " \
            + f"Player first name:{self.first_name}, " \
            + f"Player last name:{self.last_name}"\
            + f"username:{self.username}"
    
    questions=relationship("Question", secondary=track_answer, backref="players")


    #Delete player and count how many player left
    def remove_player (name):
        remove_player=session.query (Player).filter(Player.name).count ()

        if remove_player:
            session.delete(remove_player)
            session.commit()
            print (f"Player with name {name} has been removed.")
        else:
            print (f"Player with name {name} doesn't exist.")

#Add new player  

@classmethod
def new_player(cls):
    add_player= cls(first_name, last_name, username)
    add_player.save()
    return add_player

class Question (Base):
    __tablename__= 'questions'
    id = Column(Integer(), primary_key=True)
    question= Column(String())
    answer=Column (String())
    point=(Integer())
    def __repr__(self):
        return f"Question id:{self.id}: "\
            + f"Question:{self.question} "\
            + f"Answer:{self.answer}"\
            + f"Point:{self.point}"
    
    players=relationship("Player", secondary=track_answer, backref="questions")
    quizzes=relationship("Quiz", secondary=quiz_question , backref="questions")
    
    @classmethod
    def get_questions (cls, question):
       cls.all.append(question)


class Quiz (Base):
    __tablename__='quizzes'
    id = Column(Integer(), primary_key=True)
    player_id =Column(Integer(), ForeignKey ("players.id"))

    def __repr__(self):
        return f"Quiz {self.id}: " \
            + f"Player id{self.player_id}"
    
    questions=relationship("Question", secondary=quiz_question , backref="quizzes")
    