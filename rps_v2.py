print("...rock...\n")
print("...paper...\n")
print("...scissors...\n")

player1 = input("Player 1, make your move: ")
player2 = input("Player 2, make your move: ")

res1 = "Player 1 wins!"
res2 = "Player 2 wins!"
res3 = "It's a draw!"
res4 = "Something went wrong, try again."

if player1 == player2:
    print(res3)
elif player1 == "rock":
    if player2 == "scissors":
        print(res1)
    elif player2 == "paper":
        print(res2)
elif player1 == "paper":
    if player2 == "rock":
        print(res1)
    elif player2 == "scissors":
        print(res2)
elif player1 == "scissors":
    if player2 == "paper":
        print(res1)
    elif player2 == "rock":
        print(res2)
else:
    print(res4)
