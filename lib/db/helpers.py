#click 
import click
from lib.db.models import Player, Quiz, Question,track_answer, quiz_question 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine ('sqlite:///studying-VScode-shortcut-quiz.db')
Session = sessionmaker(bind=engine)
session = Session()

@click.group()

@click.option ('--count', default=0, help='Number of correct answer.')
@click.command()
def add_scores ():
    if player_input==current_question.answer:
        print ("You got correct Answer!") 
        if correct_answer:
            current_point +=1
        return current_point
    
    else:
        print ("That is incorrect, try again")
        player.question.append(current_question)

        if wrong_answer:
            current_point = 1
        return current_point
    
click.echo (f"Current Point you have: {add_scores}")



#    def add_question (question,answer):
#         question=Question (
#             question = question,
#             answer=answer
#         )
#         session.add(question)
#         session.commit ()

#     def show_question(questions):
#         print (f"Question:{questions}")
#         for question in show_question:
#             print (f"question:{question}")