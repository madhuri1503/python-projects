import random

user_count=0
computer_count=0
while True:
    user_move = input("select your choice from any of three :rock paper scissors ")
    if user_move == "stop":
        break
    else:

        actions = ["ROCK", "PAPER", "SCISSORS"]
        computer_move = random.choice(actions)
        print("user move is ", user_move)
        print("computer move is :",computer_move)
                        

        if user_move == computer_move :
            print(f"Both players selected {user_move}. It's a tie!")
        elif user_move == "ROCK":
            if computer_move == "PAPER":
                print("Paper covers the rock and computer gained a point")
                computer_count+=1
            else:
                print("rock smashes the scissors and user gained a point")
                user_count+=1

        elif user_move == "PAPER":
            if computer_move == "ROCK":
                print("Paper covers the rock and user gained a point")
                user_count+=1
            else:
                print("Scissors cut the paper into pices and compter gained a point")
                computer_count+=1

        elif user_move == "SCISSORS":
            if computer_move == "ROCK":
                print("rock smashes the scissors and Computer gained a point")
                computer_count+=1
            else:
                print("Scissors cut the paper into pices and user gained a point")
                user_count+=1


if user_count>computer_count:
    print("user won the game by",user_count-computer_count,"point")
elif user_count<computer_count:
    print("computer won the game by",computer_count-user_count,"points")
else:
    print("its a tie")

