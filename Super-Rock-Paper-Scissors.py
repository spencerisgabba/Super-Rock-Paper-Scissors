import random
import time

game_running = True
wins = 0 
loss = 0
rock_count = 0
paper_count = 0
scissor_count = 0
draws = 0
stats_list = [rock_count,paper_count,scissor_count]

# SImple Python Rock Paper Scissors Game
# By Spencer Schmidt
# E-mail: spennccee.schmidt0@gmail.com


while game_running == True:
    
    user_input = input("\nSuper Rock Paper Scissors.\n \n[P] to Play \n[S] to view stats \n[Q] to quit. \n\n> ")
    
    if user_input == "Q":
        quit()
        
    if user_input == "S":
        print("_________________")
        print("| Wins | Losses |")
        print("| ---- | ------ |")
        print("| ",wins,"  |  ",loss,"   |")
        print("_________________\n")
        
        print("You have had", draws, "draws.\n")
        print("Rock picked:", rock_count, "times.\n")
        print("Paper picked:", paper_count, "times.\n")
        print("Scissors picked:", scissor_count, "times.\n")

        input("Press Enter to go back\n")

        
    elif user_input == "P":
        list_names = ["Ron","Gary","Jakob","Pedro","Selene","Sarah","Emily"]
        
        # Array for choice list to try to get more elegant code
        
        choice_list = ['Rock','Paper','Scissors']
        
        # Menu
        my_choice = input("\n[R] for rock \n[P] for paper \n[S] for scissors. \n\n> ")
        
        time.sleep(1)        
        
        # Identifies your choice, assigns array value, adds to choice count
        
        if my_choice in ["R","ROCK","r","rock"]:
            print("\nYou have chosen Rock\n")
            current_choice = choice_list[0]
            rock_count = rock_count + 1
            time.sleep(1)

        if my_choice in ["P","PAPER","p","paper"]:
            print("\nYou have chosen Paper\n")
            current_choice = choice_list[1]
            paper_count = paper_count + 1

            time.sleep(1)

        if my_choice in ["S","SCISSOR","s","Scissor"]:
            print("\nYou have chosen Scissors\n")
            current_choice = choice_list[2]
            scissor_count = scissor_count + 1
            time.sleep(1)

        # Stopping here for check if input is legitimate

        if my_choice not in ["R","ROCK","r","rock", "P","PAPER","p","paper","S","SCISSOR","s","Scissor"]:
            print("\bPlease enter a value listed")
            time.sleep(1)        

        if my_choice in ["R","ROCK","r","rock", "P","PAPER","p","paper","S","SCISSOR","s","Scissor"]:
            
            robot_choice = random.choice(choice_list)
            
            # Random name for added humor

            print("Your opponent", random.choice(list_names), "has chosen...")
            
            # Timer for suspense
            print("..")
            time.sleep(1)
            print("...")
            time.sleep(1)
            
            print(robot_choice, "\n")
            
            time.sleep(1)

            if current_choice == robot_choice:
                print("You have reached a draw!")
                draws = draws + 1
            if current_choice == "Rock" and robot_choice == "Scissors":
                print("You Win!")
                wins = wins + 1
            if current_choice == "Paper" and robot_choice == "Rock":
                print("You Win!")
                wins = wins + 1
            if current_choice == "Scissors" and robot_choice == "Paper":
                print("You Win!")
                wins = wins + 1
            if robot_choice == "Rock" and current_choice == "Scissors":
                print("You Lose.")
                loss = loss + 1
            if robot_choice == "Paper" and current_choice == "Rock":
                print("You Lose.")
                loss = loss + 1
            if robot_choice == "Scissors" and current_choice == "Paper":
                print("You Lose.")
                loss = loss + 1