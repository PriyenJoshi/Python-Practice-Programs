import random

user_wins = 0
computer_wins = 0

options = ["rock","paper","scissors"]

while True:
    user_input = input("Enter your choice:- Rock/Paper/Scissors/Quit ").lower()
    if user_input == "quit":
        break
    if user_input not in options:
        print("Please enter from the options ")
        continue

    random_number = random.randint(0,2)
    # 0->rock 1->paper 2->scissor
    computer_select = options[random_number]
    print("Computer selected",computer_select)

    if user_input == "rock" and computer_select == "scisscor":
        print("You Won! ")
        user_wins += 1

    elif user_input == "paper" and computer_select == "rock":
        print("You Won!")
        user_wins += 1

    elif user_input == "scissors" and computer_select == "paper":
        print("You Won!")
        user_wins += 1


    elif user_input == "rock" and computer_select == "rock":
        print("Tie!")

    elif user_input == "paper" and computer_select == "paper":
        print("Tie!")

    elif user_input == "scissors" and computer_select == "scissors":
        print("Tie!")

    else:
        print("Computer Won!, You Lost :(")
        computer_wins += 1



print("You won",user_wins,"times")
print("Computer won",computer_wins,"times")
print("Goodbye see you next time")