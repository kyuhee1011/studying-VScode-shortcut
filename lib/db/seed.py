from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Player, Question, Quiz
from session import session


if __name__=='__main__':
   
    session.query(Question).delete()
    session.query(Quiz).delete()
    
    player=[]
    quizzes =[]


    questions=[
        Question (question="How do you open the terminal? ", 
                answer="ctrl + `", point=1),
        Question (question="How cut and copy/paste the line?", 
                answer="ctrl + x", point=1),
        Question (question="How do you save your work with a different name?", 
                answer="ctrl + shift + s", point=1),
        Question (question="Which key expand your screen to full screen?", 
                answer="f11", point=1),
        Question (question="How do you create a new terminal?", 
                answer="ctrl + shift + `", point=1),
        Question (question="What kind of file type is .py?", 
                answer="python", point=1),
        Question (question="What is the key to start/continue debugging the application?", 
                answer="f5", point=1),
        Question (question="What is the shortcut key to toggle line comment?", 
                answer="ctrl + /", point=1),
        Question (question="What is the shortcut key to format the document according to Visual Studio", 
                answer="shift + alt + f", point=1),
        Question (question="How do you open/learn more about Visual Studio Shortcuts?", 
                answer="ctrl + k ctrl + s", point=1)

    ]



    session.bulk_save_objects (questions, player)
    session.commit ()

    session.close()







    


