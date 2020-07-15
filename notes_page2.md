# Notes for The Modern Python 3 Bootcamp

---
Page 2

## This course is taken through [Udemy](https://www.udemy.com/course/the-modern-python3-bootcamp/)
### Instructed by [Colt Steele](https://www.udemy.com/user/coltsteele/)

---

## Rock, Paper, Scissors

**version 1** - base functionality

```python

```

first test

```
$ python3 rock_paper_scissors.py 
...rock...

...paper...

...scissors...

Player 1, make your move: rock
Player 2, make your move: paper
Player 2 wins!
$ python3 rock_paper_scissors.py 
...rock...

...paper...

...scissors...

Player 1, make your move: rock
Player 2, make your move: rock
It's a tie!
$ 
```

```python
print("...rock...\n")
print("...paper...\n")
print("...scissors...\n")

player1 = input("Player 1, make your move: ")
player2 = input("Player 2, make your move: ")


if player1 == "rock" and player2 == "scissors":
    print("Player 1 wins!")
elif player1 == "rock" and player2 == "paper":
    print("Player 2 wins!")
elif player1 == "paper" and player2 == "rock":
    print("Player 1 wins!")
elif player1 == "paper" and player2 == "scissors":
    print("Player 2 wins!")
elif player1 == "scissors" and player2 == "rock":
    print("Player 2 wins!")
elif player1 == "scissors" and player2 == "paper":
    print("Player 1 wins!")
elif player1 == player2:
    print("It's a tie!")
else:
    print("Something went wrong")
```

```
 python3 rock_paper_scissors.py 
...rock...

...paper...

...scissors...

Player 1, make your move: paper
Player 2, make your move: scissors
Player 2 wins!
$ python3 rock_paper_scissors.py 
...rock...

...paper...

...scissors...

Player 1, make your move: scissors
Player 2, make your move: paper
Player 1 wins!
$ python3 rock_paper_scissors.py 
...rock...

...paper...

...scissors...

Player 1, make your move: 
Player 2, make your move: fd
Something went wrong
$ python3 rock_paper_scissors.py 
...rock...

...paper...

...scissors...

Player 1, make your move: scissors
Player 2, make your move: scissors
It's a tie!
$ 
```

**verison 2** - refactored

```python
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

```

```
$ python3 rock_paper_scissors.py 
...rock...

...paper...

...scissors...

Player 1, make your move: paper
Player 2, make your move: scissors
Player 2 wins!
$ python3 rock_paper_scissors.py 
...rock...

...paper...

...scissors...

Player 1, make your move: scissors
Player 2, make your move: paper
Player 1 wins!
$ python3 rock_paper_scissors.py 
$ python3 rps_v2.py 
...rock...

...paper...

...scissors...

Player 1, make your move: rock
Player 2, make your move: paper
Player 2 wins!
$ python3 rps_v2.py 
...rock...

...paper...

...scissors...

Player 1, make your move: rock
Player 2, make your move: scissors
Player 1 wins!
$ python3 rps_v2.py 
...rock...

...paper...

...scissors...

Player 1, make your move: scissors
Player 2, make your move: paper
Player 1 wins!
$ python3 rps_v2.py 
...rock...

...paper...

...scissors...

Player 1, make your move: scissors
Player 2, make your move: rock
Player 2 wins!
$ python3 rps_v2.py 
...rock...

...paper...

...scissors...

Player 1, make your move: paper
Player 2, make your move: rock
Player 1 wins!
$ python3 rps_v2.py 
...rock...

...paper...

...scissors...

Player 1, make your move: paper
Player 2, make your move: scissors
Player 2 wins!
$ python3 rps_v2.py 
...rock...

...paper...

...scissors...

Player 1, make your move: rock
Player 2, make your move: rock
$ python3 rps_v2.py 
...rock...

...paper...

...scissors...

Player 1, make your move: fd
Player 2, make your move: rock
Something went wrong, try again.
$ python3 rps_v2.py 
...rock...

...paper...

...scissors...

Player 1, make your move: SCISSORS
Player 2, make your move: rock
Something went wrong, try again.
$ 
```

**version 3** - conputer player

*import **random***

```python
import random

# print("Rock...")
# print("Paper...")
# print("Scissors...")

# player1 = input("(Emter your choice): ")
rand_num = random.randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
print(computer) 
```

```
$ python3 rps_v3.py 
paper
$ python3 rps_v3.py 
paper
$ python3 rps_v3.py 
rock
$ python3 rps_v3.py 
scissors
$ 
```

```python
import random

print("Rock...")
print("Paper...")
print("Scissors...")

player = input("(Emter your choice): ")
rand_num = random.randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
print(f"Computer) 

res1 = "Player wins!"
res2 = "Computer wins!"
res3 = "It's a draw!"
res4 = "Something went wrong, try again."

if player == computer:
    print(res3)
elif player == "rock":
    if computer == "scissors":
        print(res1)
    elif computer == "paper":
        print(res2)
elif player == "paper":
    if computer == "rock":
        print(res1)
    elif computer == "scissors":
        print(res2)
elif player == "scissors":
    if computer == "paper":
        print(res1)
    elif computer == "rock":
        print(res2)
else:
    print(res4)
```

```
$ python3 rps_v3.py 
Rock...
Paper...
Scissors...
(Emter your choice): rock
rock
It's a draw!
$ python3 rps_v3.py 
Rock...
Paper...
Scissors...
(Emter your choice): rock
scissors
Player wins!
$ python3 rps_v3.py 
Rock...
Paper...
Scissors...
(Emter your choice): rock
paper
Computer wins!
$ python3 rps_v3.py 
Rock...
Paper...
Scissors...
(Emter your choice): paper
paper
It's a draw!
$ python3 rps_v3.py 
Rock...
Paper...
Scissors...
(Emter your choice): PAPER
scissors
Something went wrong, try again.
$ 
```

*made **case insensitive***

```python
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
```

```
$ python3 rps_v3.py 
Rock...
Paper...
Scissors...
(Emter your choice): ROCK
Computer plays rock
It's a draw!
$ python3 rps_v3.py 
Rock...
Paper...
Scissors...
(Emter your choice): PapeR
Computer plays scissors
Computer wins!
$ python3 rps_v3.py 
Rock...
Paper...
Scissors...
(Emter your choice): sciSSors  
Computer plays scissors
It's a draw!
$ 
```

---

## Looping in Python

### *for* Loops

In python, ***for*** loops are written like this:

```python
for item in iterable_object:
    # do something with item
```

- An iterable object is some kind of collection of items, for instance: a list of numbers, a string of characters, a range, etc.
- *item* is a new variable that can be called whatever you want
- *item* references the current position of our **iterator** within the *iterable*. It will iterate over (run through) every item of the collection and then go away when it has visited all items


*for* loops with ranges

```python
for number in range(1, 8):
    print(number)
```

```python
for x in range(1,10):
    print(x)
```
```
3 for.py 
1
2
3
4
5
6
7
8
9
```

```python
for x in range(1,10):
    print(x)
    print(x*x)
```
```
 python3 for.py 
1
1
2
4
3
9
4
16
5
25
6
36
7
49
8
64
9
81
```

```python
for char in "coffee":
    print(char)
```
```
$ python3 for.py 
c
o
f
f
e
e
```

```python
for char in "coffee":
    print(char*10)
```
```
$ python3 for.py 
cccccccccc
oooooooooo
ffffffffff
ffffffffff
eeeeeeeeee
eeeeeeeeee
```