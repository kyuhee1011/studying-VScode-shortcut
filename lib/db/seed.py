from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Player, Question, Quiz
import random


engine = create_engine('sqlite:///studying-VScode-shortcut-quiz.db')
Session = sessionmaker(bind=engine)
session = Session()

  
session.query(Player).delete()
session.query(Question).delete()
session.query(Quiz).delete()



users=[]
quizzes =[]
questions=[
    Question (question="How do you open the terminal? ", 
              answer="ctrl + `", points="1"),
    Question (question="How cut and copy/paste the line?", 
              answer="ctrl + x", points="1"),
    Question (question="How do you save your current work to your current file?", 
              answer="ctrl + shift + s", points="1"),
    Question (question="How do you save your work with a different name?", 
              answer="ctrl + s", points="1"),
    Question (question="Which key expand your screen to full screen?", 
              answer="f11", points="1"),
    Question (question="How do you open the search bar?", 
              answer="ctrl + shift + f", points="1"),
    Question (question="How do you create a new terminal?", 
              answer="ctrl + shift + `", points="1"),
    Question (question="What kind of file type is .py?", 
              answer="Python", points="1"),
    Question (question="What is the key to start/continue debugging the application?", 
              answer="f5", points="1"),
    Question (question="What is the shortcut key to create a new file?", 
              answer="ctrl + n", points="1"),
    Question (question="What is the shortcut key to toggle line comment?", 
              answer="ctrl + /", points="1"),
    Question (question="What is the shortcut key to quickly navigate to a method's definition in Visual Studio? ", 
              answer="f12", points="1"),
    Question (question="What is the shortcut key to format the document according to Visual Studio", 
              answer="shift + alt + f"),
    Question (question="What is the shortcut key to undo last cursor operation?", 
              answer="ctrl + u", points="1"),
    Question (question="What is the shortcut key to close the currently selected tab in Visual Studio?", 
              answer="ctrl + f4", points="1"),
    Question (question="What is the shortcut key to open the Error List window in Visual Studio?", 
              answer="ctrl + e", points="1"),
    Question (question="How do you open user setting?", 
              answer="ctrl + ,", points="1"),
    Question (question="How do you open/learn more about Visual Studio Shortcuts?", 
              answer="ctrl + k ctrl + s", points="1")

]



session.bulk_save_objects (questions)
session.commit ()



