import time
from sqlalchemy import create_engine
from models import Player, Question, Quiz, track_answer,quiz_question
from simple_term_menu import TerminalMenu
from sqlalchemy.orm import sessionmaker
from prettycli import red, green, yellow, blue
from session import session
#prettycli

class Cli:
    def __init__ (self, current_player=None):
        self.current_player=current_player
        self.questions= session.query(Question).all()

        #assign as 0 to ask question from the beginning (add next_question function to go to ask next question)
        self.track_index = 0
        # import ipdb; ipdb.set_trace()

    #start menu 
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
        username=input ("Enter your username")
        existing_player=session.query(Player).filter_by(username=username).first()
        print (existing_player)
        if existing_player:
            self.current_player=existing_player
            self.show_start_options()
        else:
            print (red("Username was not found. Would like to sign up and start the game?"))
            response = input("Enter 'yes' to continue:")
            if response=="yes":
                self.enter_addMe()
            else:
                self.handle_exit()

    def enter_addMe (self):
        first_name = input("What is your first name?")
        last_name = input("What is your last name?")
        username = input("Enter your username")

        new_player= Player.new_player(first_name, last_name, username)
        self.current_player=new_player
        self.show_start_options ()       
       
#start quiz menu option
    def show_start_options(self):
        quiz_menu_options =["Start the Quiz", "View all questions", "My Score", "Remove Me", "Exit"]
        quiz_start_menu = TerminalMenu(quiz_menu_options) 
       
        quiz_index=quiz_start_menu.show()
        if quiz_menu_options[quiz_index]=="Start the Quiz":
            self.handle_start()
        elif quiz_menu_options[quiz_index]=="View all questions":
            self.show_all_questions()
        elif quiz_menu_options[quiz_index]== "My Score":
            self.show_score()
        elif quiz_menu_options[quiz_index]== "Remove Me":
            self.handle_remove_user()
        else: self.handle_exit()
    
    def handle_remove_user(self):
        username = input("Enter your username")
        Player.remove_player(session, username)
        if self.current_player==username:
            self.current_player
        self.start_quiz ()       
    
    def clear_lines(self):
        print ("\n"*10)
    
    def handle_start (self):
        print (blue("Quiz started"))
        question=self.questions[self.track_index]
        print(f"Question: {question.question}")
        self.track_answer()
        
    def track_answer(self):
       
        question = self.questions[self.track_index] 
        player_input = input("Enter your answer: ")
        if player_input == question.answer:
            print(green("That is correct!"))
            self.current_player.point += question.point
            self.next_question()  
        else:
            print(red("That is incorrect!"))

            #Object relationship method
            #this part utilizes the many-to-many relaionship set up earlier to handle 
            #the connection between the Player and the Question
            self.current_player.questions.append(question)
             #invoke next_question whether a player got correct or incorrect
            self.next_question()  
       
            session.add(self.current_player)
            session.commit()          
  
        return self.track_index
    
    def next_question(self):
        #create variable to compare on player input     
        player_input=input("Enter 'n' for next question or 'any key' to exit")
        #if player input is "n" then question increment
        if player_input.lower()=='n':
            self.track_index += 1
            
            question=self.questions[self.track_index]
            print(f"Question: {question.question}")
            self.track_answer()
                     
        else: 
            
            self.handle_exit()

    def show_score (self):
        
        highest_score=session.query(Player).order_by(Player.point.desc()).first()
        #use dictionary to show player who has highest score
        highest_player = {
            "Username": highest_score.username,
            "Score": highest_score.point
        }
        print("The Player with the Highest Score is:",highest_player)
        total_score=self.current_player.point

        print(f"Total Score for 'username': {self.current_player.username}, 'score': {total_score}")

        #add start menu option to choose the menu
        self.show_start_options()

    def show_all_questions(self):
        #used count() aggregation to tell player how many total questions there are 
        questions_count= session.query(Question).count()
        print (yellow (f"Total Questions are: {questions_count}"))

        #used list to show all questions
        questions = session.query(Question).all()
        for question in questions:
            print(f"Question:{question.question}")
        time.sleep(7)
        self.clear_lines()
        self.show_start_options()

    

    def handle_exit (self):
        print (blue ('Good Bye'))          

if __name__ == '__main__':
    # pass
    app=Cli()
    app.start_quiz()
