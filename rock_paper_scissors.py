'#A rock paper scissors game bye Rhetthenry on github'
import random

player = input("what is your choice? ")

computer = random.choice(["rock", "paper", "scissors", "peach"])

print(computer)

if player == computer:
    print("Its a tie ")
elif player == "rock" and computer == "scissors":
    print("You win!")
elif player == "scissors" and computer == "paper":
    print("You win")
elif player == "paper" and computer == "rock":
    print("You win!")
elif player == "peach" and computer == "paper":
    print("You win!")
elif player == "rock" and computer == "peach":
    print("You win!")
elif player == "peach" and computer == "scissors":
    print("You win!")

else:
    print("You lost....Please play agin")
