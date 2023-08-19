#click 
import click
from models import Player, Quiz, Question,track_answer, quiz_question 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine ('sqlite:///studying-VScode-shortcut-quiz.db')
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    pass

@click.option ('--count', default=0, help='Number of correct answer.')
@click.command()
def add_scores (self):
    count =self.track_answer.points
    if player_input==correct_answer.answer:
        print ("You got correct Answer!") 
        count+=1   
    else:
        print ("That is incorrect, try again")
    
    click.echo (f"Current Point you have: {count}")
    

if __name__ == '__main__':
    cli()
    add_scores()



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