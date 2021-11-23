import random


computer_choice = random.choice(['rock', 'paper', 'scissors'])

user_choice = input("Choose rock, paper or scissors\n")

if computer_choice == user_choice:
    print("Tie")

elif computer_choice == "scissors" and user_choice == "rock":
    print("You win")

elif computer_choice == "rock" and user_choice == "paper":
    print("You win")

elif computer_choice == "paper" and user_choice == "scissors":
    print("You win")

else:
    print("You lose.")

