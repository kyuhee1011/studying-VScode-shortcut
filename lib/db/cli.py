
from sqlalchemy import create_engine
from models import Player
from simple_term_menu import TerminalMenu
from sqlalchemy.orm import sessionmaker

engine = create_engine ('sqlite:///studying-VScode-shortcut-quiz.db')
Session = sessionmaker(bind=engine)
session = Session()

class Start:
    def __init__ (self):
        current_player=None

    def start_quiz (self):
        start_menu_options= ["Enter username", "AddMe", "Exit"]
        start_menu=TerminalMenu(start_menu_options)
        start_index=start_menu.append ()
        if start_menu_options[start_index] == "Enter username":
            self.enter_username()
        elif start_menu_options[start_index]=="AddMe":
            self.enter_addMe()
        else: self.handle_exit

    def enter_username(self):
        username=username
        username=Player.username.find(username=username)
        
        if username:
            self.username=username
            self.show_start_options
        else:
            print ("Username was not found. Would like to sign up and start the game?")
            yes = yes
            if yes:
                self.enter_addMe
            else:
                self.handle_exit

    def enter_addMe (self,first_name, last_name, username):
        session=Session()
        add_player= Player (session, first_name=first_name, last_name=last_name, username=username)
        
        print(f'Welcome {add_player} start the quiz')

        self.handle_start ()       

    def show_start_options(self):
        quiz_menu_options =["Start the Quiz", "My Score", "Exit"]
        quiz_start_menu = TerminalMenu (quiz_menu_options)
        quiz_index=quiz_start_menu.append()
        if quiz_start_menu [quiz_index]=="Start the Quiz":
            self.handle_start
        elif quiz_start_menu [quiz_index]== "My Score":
            self.show_score
        else: self.handle_exit

    def handle_start (self):
        print("Quiz started and please enter your answer")




    def show_score (self):
        pass


    def handle_exit (self):
        print ("Good Bye")          

if __name__=='main':
    app=Start()
    app.start()