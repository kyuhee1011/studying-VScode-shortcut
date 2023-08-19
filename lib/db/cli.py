
from sqlalchemy import create_engine
from models import Player, Question, Quiz, track_answer,quiz_question
from simple_term_menu import TerminalMenu
from sqlalchemy.orm import sessionmaker

engine = create_engine ('sqlite:///studying-VScode-shortcut-quiz.db')
Session = sessionmaker(bind=engine)
session = Session()

class Cli:
    def __init__ (self, current_player=None):
        current_player=current_player
       

    def start_quiz (self):
        start_menu_options= ["Enter username", "AddMe", "Exit"]
        start_menu=TerminalMenu(start_menu_options)
        start_index=start_menu.show ()
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

    def enter_addMe (self):
        first_name = input ("What is your first name?")
        last_name =input ("What is your last name?")
        username=input("Enter your username")
        new_player= Player (first_name=first_name, last_name=last_name, username=username)
        print(f'Welcome {new_player.username} start the quiz')
     
        session.add (new_player)
        session.commit()

        self.show_start_options ()       
       

    def show_start_options(self):
        quiz_menu_options =["Start the Quiz", "View all questions", "My Score", "Exit"]
        quiz_start_menu = TerminalMenu (quiz_menu_options)
        quiz_index=quiz_start_menu.show()
        if quiz_start_menu =="Start the Quiz":
            self.handle_start()
        elif quiz_start_menu=="View all questions":
            self.show_all_questions()
        elif quiz_start_menu == "My Score":
            self.show_score()
        else: self.handle_exit()
    
    def clear_lines(self):
        print ("\n"*20)
    
    def handle_start (self):
        print ("Quiz started")
        # question=Question.get_question()
        # print(f"Question: {self.question}")
        # for question in questions:
        #     answer= input ()
        #     self.track_answer()

    def track_answer(self, current_player, answer):
        point=0
        self.player_input= current_player
        if self.player_input == answer: 
            self.point +=1
            self.show_score()
        else:
            self.handle_exit()


    def show_score (self, current_player):
        current_player=[]
        total_score=sum(point["point"] for point in Question)
        current_player.append = {
                "username":current_player.username,
                "Score":current_player.point
            }
        
        return total_score

    def show_all_questions (self):
        print("hello")

        # self.show_start_options ()    
        # questions=Question.get_questions
        # self.clear_lines()
        # self.show_start_options()      

    def handle_exit (self):
        print ("Good Bye")          

if __name__=='__main__':
    app=Cli()
    app.start_quiz()