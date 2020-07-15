import random

print("Rock...")
print("Paper...")
print("Scissors...")

player = input("Player, make your move: ").lower()
rand_num = random.randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
print(f"Computer plays {computer}") 

res1 = "You win!"
res2 = "Computer wins!"
res3 = "It's a draw!"
res4 = "Please enter a valid move."

if player == computer:
    print(res3)
elif player == "rock":
    if computer == "scissors":
        print(res1)
    else:
        print(res2)
elif player == "paper":
    if computer == "rock":
        print(res1)
    else:
        print(res2)
elif player == "scissors":
    if computer == "paper":
        print(res1)
    else:
        print(res2)
else:
    print(res4)
