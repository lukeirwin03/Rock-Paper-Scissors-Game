import random

choices = ["rock", "paper", "scissors"]

computer = None
player = None
win = False
pWins = 0
cWins = 0
repeat = True

while repeat == True:
    while win == False:
        computer = random.choice(choices)
        player = input("Rock, Paper, or Scissors? : ").lower()
        
        if player == computer:
            print("computer: " , computer)
            print("player: ",player)
            print("Tie Game!")
            win = True
        elif player == "rock":
            if computer == "paper":
                print("Paper covers Rock! \nComputer Wins!")
                cWins += 1
                win = True
            elif computer == "scissors":
                print("Rock crushes Scissors! \nPlayer Wins!")
                pWins += 1
                win = True
        elif player == "paper":
            if computer == "scissors":
                print("Scissors cut Paper! \nComputer Wins!")
                cWins += 1
                win = True
            elif computer == "rock":
                print("Paper covers Rock! \nPlayer Wins!")
                pWins += 1
                win = True
        elif player == "scissors":
            if computer == "rock":
                print("Rock crushes Scissors! \nComputer Wins!")
                cWins += 1
                win = True
            elif computer == "paper":
                print("Scissors cut Paper! \nPlayer Wins!")
                pWins += 1
                win = True
    print("Player Score: ", pWins, "\nComputer Score: ", cWins)
    win = False
    playAgain = input("Would you like to play again? [y,n]")
    if playAgain == "n":
        repeat = False