# A simple rock, paper, scissors game that takes input from the user so they may
    # compete against a randomly generated game move from the computer to
    # determine a winner

# Import the random library to generate random numbers
import random

# Create a list of options for the user to select from
game_options = ["r", "p", "s"]

# Get the choice from the computer and set it to a variable, passing the list as the choices
computer_play = random.choice(game_options)

# Introduce the game to the user
print("Time to play rock, paper, scissors! Test your luck against the computer.")
print("------------------------------------------------------------------------")

# Get input from the user for their choice in the round
user_play = input("Make your choice! (r)ock, (p)aper, or (s)cissors? ")

# Set the condition for the while loop
continue_game = "y"

# While loop that will let the user dictate how many rounds the game has
while continue_game == "y":
    # Else-if statement that determines the outcome of the game based on the user's choice
    # Nest else-if statements that will give the outcome based on the computer's choice
    if (user_play == "r" or user_play == "r"):
        if (computer_play == "r"):
            print("You selected rock and the computer selected rock. Tie match!")
            continue_game = input("Would you like to play again? y/n? ")
            if continue_game == "y":
                user_play = input("Make your choice! (r)ock, (p)aper, or (s)cissors? ")
                print("------------------------------------------------------------------------")
        elif (computer_play == "p"):
            print("You selected rock and the computer selected paper. You lose!")
            continue_game = input("Would you like to play again? y/n? ")
            if continue_game == "y":
                user_play = input("Make your choice! (r)ock, (p)aper, or (s)cissors? ")
                print("------------------------------------------------------------------------")
        elif (computer_play == "s"):
            print("You selected rock and the computer selected scissors. You win!")
            continue_game = input("Would you like to play again? y/n? ")
            if continue_game == "y":
                user_play = input("Make your choice! (r)ock, (p)aper, or (s)cissors? ")
                print("------------------------------------------------------------------------")
    elif (user_play == "p" or user_play == "P"):
        if (computer_play == "r"):
            print("You selected paper and the computer selected rock. You win!")
            continue_game = input("Would you like to play again? y/n? ")
            if continue_game == "y":
                user_play = input("Make your choice! (r)ock, (p)aper, or (s)cissors? ")
                print("------------------------------------------------------------------------")
        elif (computer_play == "p"):
            print("You selected paper and the computer selected paper. Tie match!")
            continue_game = input("Would you like to play again? y/n? ")
            if continue_game == "y":
                user_play = input("Make your choice! (r)ock, (p)aper, or (s)cissors? ")
                print("------------------------------------------------------------------------")
        elif (computer_play == "s"):
            print("You selected paper and the computer selected scissors. You lose!")
            continue_game = input("Would you like to play again? y/n? ")
            if continue_game == "y":
                user_play = input("Make your choice! (r)ock, (p)aper, or (s)cissors? ")
                print("------------------------------------------------------------------------")
    elif (user_play == "s" or user_play == "S"):
        if (computer_play == "r"):
            print("You selected scissors and the computer selected rock. You lose!")
            continue_game = input("Would you like to play again? y/n? ")
            if continue_game == "y":
                user_play = input("Make your choice! (r)ock, (p)aper, or (s)cissors? ")
                print("------------------------------------------------------------------------")
        elif (computer_play == "p"):
            print("You selected scissors and the computer selected paper. You win!")
            continue_game = input("Would you like to play again? y/n? ")
            if continue_game == "y":
                user_play = input("Make your choice! (r)ock, (p)aper, or (s)cissors? ")
                print("------------------------------------------------------------------------")
        elif (computer_play == "s"):
            print("You selected scissors and the computer selected scissors. Tie match!")
            continue_game = input("Would you like to play again? y/n? ")
            if continue_game == "y":
                user_play = input("Make your choice! (r)ock, (p)aper, or (s)cissors? ")
                print("------------------------------------------------------------------------")
    else:
        print("Invalid input! Please try again.")
        continue_game = input("Would you like to try again? y/n? ")

