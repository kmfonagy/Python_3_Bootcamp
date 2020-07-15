# Notes for The Modern Python 3 Bootcamp

---
Page 1

## This course is taken through [Udemy](https://www.udemy.com/course/the-modern-python3-bootcamp/)
### Instructed by [Colt Steele](https://www.udemy.com/user/coltsteele/)

---

## Basics

print() returns something like:

```python
print("Hello World!")
Hello World!
```

Fractions are __always__ returned as a float

```python
print("3/4 =", 3/4)
3/4 = 0.75
```

** means to the power of, like 2^3. When you use a fraction, it's the root

```python
print("2**3 =", 2**3)
2**3 = 8
```

Using % (modulo) provides the remainder of the initial number minus from the second

```python
print("10%3 =", 10%3)
10%3 = 1
```

// rounds down to return an int regardless

```python
print("10//3 =", 10//3)
10//3 = 3
```

Creating a variable stores the given value

```python
cash = 19867324678987.99
cash = cash/5
print("$" + str(cash))
$3973464935797.5977
```

---

### Naming conventions:

* Snake Case (snake_case) is preferred, though Camel Case (camelCase) is accepted
* CAPITAL_SNAKE_CASE refers to a constant, like PI = 3.14
* UpperCamelCase refers to a class
* Dunders (double underscore) '__dunder__' refers to private variables

### Naming restrictions:

1. Must start with a letter or '_'
1. rest of the name must consist of letters, numbers, or underscores
1. variable names are case sensitive; DOGS != Dogs || Dogs != dogs

__Data types__ | __Description__
---|---
bool | boolean data type (True/False)
int | a number (1, 2, 3, etc)
float | a number with fraction (1.5, 3.666, 10.75, etc)
str | (string) a sequence of Unicode Characters
list | an ordered sequence of values of other data types ([1, 2, 3] or ['a', 'b', 'c'])
dict | a collection of key: values ({'first_name': 'f_name', 'last_name': 'l_name'})

Python uses __dynamic typing__: meaning variables can easily change

```python
name = "Your Name"
print(name)
'Your Name'
name = 13
print(name)
13
```

*With other coding languages, you must declare the variable type ahead of the variable name: int num = 13, String name = "Your Name"*

### None

__None__ is a special value. It represents nothing, Python's version of _null_

### [String Escape Sequences](http://www.python-ds.com/python-3-escape-sequences)

* To break into a new line use 

```python
print("This \\n breaks into a\nnewline")
```
'This \n breaks into a
newline'

* To add a backslash to text

```python
print("This \\\\ ads a backslash (\\)")
```
'This \\\\ ads a backslash (\\)'

* To add single or double quotations

```python
print("Use \\\' for a \'single\' quotation mark or apostrophe,\nand \\\" for \"double\" quotation marks")
```
'Use \\' for a 'single' quotation mark or apostrophe,
and \\" for "double" quotation marks

### String concatenation

```python
str_one = "eat"
str_two = "food"
str_three = str_one + " " + str_two
print(str_three)
```
'eat food'

*simpler way*

```python
str_1 = "ice"
str_1 += " cream"
print(str_1)
```
'ice cream'

### Converting Data Types

```python
num = 5
float(num)
```
5.0

```python
num = 32
str(num)
```
'32'

---

## Simple Converter Program

```python
int("How many kilometers did you run today?")
kms = float(input())
miles = kms/1.60934
miles = round(miles, 2)
print(f"\nYour {kms} km run is equal to {miles} mi!\n")
```

    PS C:\..\Python 3 Course> python .\milage_convertor.py

    How many kilometers did you run today?
    47
    
    Your 47.0 km run is equal to 29.2 mi!

---

## Boolean and Conditional Logic

### Getting User Input

    PS C:\..\Python 3 Course> python

        >>> name = input("Enter your name here: ")
    Enter your name here: Tyrion Lanister
    >>> print(name)
    Tyrion Lanister

```python
data = input("What\'s your favorite color?")
print("Your favorite color is " + data)

print()

print("What\'s your favorite color?")
data = input()
print("Your favorite color is " + data)
```
    PS C:\..\Python 3 Course> python .\input.py

    hat's your favorite color?blue
    Your favorite color is blue

    What's your favorite color?
    green
    Your favorite color is green

### Intro to Conditionals

**if** *some condition is True:*
    do something
**elif** *some other condition is True:*
    do something
**else**:
    do something

```python
print("What is your name?")
name = input()
if name == "Arya Stark":
    print("Valar Morghulis")
elif name == "Jon Snow":
    print("You know nothing")
else:
    print("Carry on")
```
```
PS C:\..\Python 3 Course> python .\conditional.py

What is your name?
Jon Snow
You know nothing
PS C:\..\Python 3 Course> python .\conditional.py

What is your name?
Arya Stark
Valar Morghulis
PS C:\..\Python 3 Course> python .\conditional.py

What is your name?
jon snow
Carry on
```
*The last attempt shows case sensitivity*

### Exercises

```python
# NO TOUCHING PLEASE---------------
from random import randint
choice = randint(1,10)
# NO TOUCHING PLEASE---------------

# YOUR CODE GOES HERE:
if choice == 7:
    print("lucky")
else:
    print("unlucky")
```
:heavy_check_mark: **Well done, your solution is correct!**

```python
# NO TOUCHING ======================================
from random import randint
num = randint(1, 1000) #picks random number from 1-1000
# NO TOUCHING ======================================



# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
if num % 2 != 0:
    print("odd")
else:
    print("even")

# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```
:heavy_check_mark: **Well done, your solution is correct!**

### Multiple elifs

```python
color = input("What\'s your favorite color?")
if color == 'purple':
    print("excellent choice!")
elif color == 'teal':
    print("not bad!")
elif color == 'seafoam':
    print("mediocre")
elif color == 'pure darkness':
    print("I like how you think")
else:
    print("YOU MONSTER!")
```

```
PS C:\..\Python 3 Course> python .\conditional.py

What's your favorite color?purple
excellent choice!
PS C:\..\Python 3 Course> python .\conditional.py

What's your favorite color?teal
not bad!
PS C:\..\Python 3 Course> python .\conditional.py

What's your favorite color?seafoam
mediocre
PS C:\..\Python 3 Course> python .\conditional.py

What's your favorite color?pure darkness
I like how you think
PS C:\..\Python 3 Course> python .\conditional.py

What's your favorite color?blue
YOU MONSTER!
```

### Truthiness

```python
x = 1
x is 1 # True
x is 0 # False
```
We can call values that will resolve to True **"truthy**, or values that will resolve to False **"falsy"**.

Besides False conditional checks, other things that are naturally falsy include: empty objects, empty strings, *None*, and zero.

```python
print("enter your favorite animal")
animal = input()
if animal:
    print(animal + " is my favorite too!")
else:
    print("YOU DIDN\'t SAY ANYTHING!")
```
```
PS C:\..\Python 3 Course> python .\truthiness.py

enter your favorite animal
dog
dog is my favorite too!
PS C:\..\Python 3 Course> python .\truthiness.py

enter your favorite animal
bob
bob is my favorite too!
PS C:\..\Python 3 Course> python .\truthiness.py

enter your favorite animal

YOU DIDN't SAY ANYTHING!
```

### Comparison Operators

**Op** | **What it does** | **Example**
---|---|---
**==** | Truthy if **a** has the same value as **b** | a **==** b # True
**!=** | Truthy if **a** does **NOT** have the same value as **b** | a **!=** b # False
**>** | Truthy if **a** is greater than **b** | a **>** b # False
**<** | Truthy if **a** is less than **b** | a **<** b # False
**>=** | Truthy if **a** is greater than or equal to **b** | a **>=** b # True
**<=** | Truthy if **a** is less than or equal to **b** | a **<=** b # True

```
PS C:\..\Python 3 Course> python

>>> 1==1
True
>>> 1==2
False
>>> 1!=2
True
>>> "a" == "A"
False
>>> 1>2
False
>>> 3>2
True
>>> 1<2
True
>>> 4<2
False
>>> 1>=2
False
>>> 2>=2
True
>>> 1<=2
True
>>> 14<=2
False
```

### Logical AND & OR

**Op** | **What it does** | **Example**
---|---|---
and | Truthy if both **a** AND **b** are true (logical conjunction) | **if** a **and** b: print(c)
or | Truthy if either **a** OR **b** are true (logical disjunction) | **if** a **or** b: print(c)
not | Truthy if the opposite of **a** is is true (logical negation) | **if not** a: print(b)

#### AND

```python
a = "3"
print("What number am I thinking of between 1 & 10?")
b = input()
if a and b == "3":
    print("You\'re right!")
else:
    print("NO!")
```
```
PS C:\..\Python 3 Course> python .\truthiness.py

What number am I thinking of between 1 & 10?
3
You're right!
PS C:\..\Python 3 Course> python .\truthiness.py

What number am I thinking of between 1 & 10?
5
NO!
```

#### OR

```python
print("What\'s your favorite movie franchise?")
movie = input()
if movie == "indiana jones" or movie == "star wars":
    print("You have good taste!")
else:
    print("Ehhh")
```
```
PS C:\..\Python 3 Course> python .\truthiness.py

What's your favorite movie franchise?
twilight
Ehhh
PS C:\..\Python 3 Course> python .\truthiness.py

What's your favorite movie franchise?
star wars
You have good taste!
```

### Exercise

```python
# NO TOUCHING ============================================
from random import choice
food = choice(['apple','grape', 'bacon', 'steak', 'worm', 'dirt'])
# NO TOUCHING =============================================


# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

if food == "apple" or food == "grape":
    print("fruit")
elif food == "bacon" or food == "steak":
    print("meat")
elif food == "dirt" or food == "worm":
    print("yuck")

# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```
:heavy_check_mark: **Well done, your solution is correct!**

#### NOT

**Example**

```
>>> age = 10
>>> age < 4
False
>>> not age < 4
True
```
```python
age = 21

# 2-8 2 dollar ticket
# 65+ 5 dollar ticket
# 10 dallar ticket

if not ((age >= 2 and age <= 8) or age >= 65):
    print("You pay $10 and are not a child or senior.")
```

```
$ python3 not.py
You pay $10 and are not a child or senior.
```

```python
age = 7

# 2-8 2 dollar ticket
# 65+ 5 dollar ticket
# 10 dallar ticket

if not ((age >= 2 and age <= 8) or age >= 65):
    print("You pay $10 and are not a child or senior.")
else:
    print("You are a child or senior.")
```

```
$ python3 not.py
You are a child or senior.
```

```
>>> 1 < 2
True
>>> not 1 < 2
False
>>> not (1 > 3 and 5==5)
True
```

### is VS ==

**is** only works when the variable is pointing to the **same** item in memory.

```python
a = 1
a == 1 # True
a is 1 # True

a = [1, 2, 3] # a list of numbers
b = [1, 2, 3]
a == b # True
a is b # False

c = b
b is c # True
```

### Bouncer Code-Along

```python
# ask for age
age = input("How old are you: ")

# will cause typeerror, so need to cast 'age' as int
if int(age) >= 18 and int(age) < 21:
    print("You can enter, but need a wristband!")
# 18-21 wristband
# 21+ drink, normal entry
# too young, sorry
```

```
$ python3 bouncer.py 
How old are you: 19
You can enter, but need a wristband!
$ python3 bouncer.py 
How old are you: 2
$ 
```

```python
# ask for age
age = input("How old are you: ")

# will cause typeerror, so need to cast 'age' as int
# 18-21 wristband
if int(age) >= 18 and int(age) < 21:
    print("You can enter, but need a wristband!")
# 21+ drink, normal entry
elif int(age) >= 21:
    print("You are good to enter, and are able to drink.")
# too young, sorry
```

```
$ python3 bouncer.py 
How old are you: 23
You are good to enter, and are able to drink.
```

```python
# ask for age
age = input("How old are you: ")

# will cause typeerror, so need to cast 'age' as int
# 18-21 wristband
if int(age) >= 18 and int(age) < 21:
    print("You can enter, but need a wristband!")
# 21+ drink, normal entry
elif int(age) >= 21:
    print("You are good to enter, and are able to drink.")
# too young, sorry
else:
    print("You are not old enough to come in.")
```

```
$ python3 bouncer.py 
How old are you: 12
You are not old enough to come in.
```

*Problem will occur if the user returns an empty string*

```
$ python3 bouncer.py 
How old are you: 
Traceback (most recent call last):
  File "bouncer.py", line 6, in <module>
    if int(age) >= 18 and int(age) < 21:
ValueError: invalid literal for int() with base 10: ''
```

```python
# ask for age
age = input("How old are you: ")

# will cause typeerror, so need to cast 'age' as int
# check for int
if age != "":
    # 18-21 wristband
    if int(age) >= 18 and int(age) < 21:
        print("You can enter, but need a wristband!")
    # 21+ drink, normal entry
    elif int(age) >= 21:
        print("You are good to enter, and are able to drink.")
    # too young, sorry
    else:
        print("You are not old enough to come in.")
else:
    print("Please enter an age.")
```

*Alternatively, check if it is truthy*

```python
# ask for age
age = input("How old are you: ")

# will cause typeerror, so need to cast 'age' as int
# check for int
if age:
    # 18-21 wristband
    if int(age) >= 18 and int(age) < 21:
        print("You can enter, but need a wristband!")
    # 21+ drink, normal entry
    elif int(age) >= 21:
        print("You are good to enter, and are able to drink.")
    # too young, sorry
    else:
        print("You are not old enough to come in.")
else:
    print("Please enter an age.")
```

**Change it so that it casts as int prior to *if* statements**

```python
# ask for age
age = input("How old are you: ")

# will cause typeerror, so need to cast 'age' as int
# check for int
if age:
    age = int(age)
    # 18-21 wristband
    if age >= 18 and age < 21:
        print("You can enter, but need a wristband!")
    # 21+ drink, normal entry
    elif age >= 21:
        print("You are good to enter, and are able to drink.")
    # too young, sorry
    else:
        print("You are not old enough to come in.")
else:
    print("Please enter an age.")
```

```
$ python3 bouncer.py 
How old are you: 19
You can enter, but need a wristband!
$ python3 bouncer.py 
How old are you: 21
You are good to enter, and are able to drink.
$ python3 bouncer.py
How old are you: 5
You are not old enough to come in.
$ python3 bouncer.py 
How old are you: 
Please enter an age.
```

*Indentation really matters for the **if** statements to work*

More efficiently:

```python
# ask for age
age = input("How old are you: ")

# will cause typeerror, so need to cast 'age' as int
# check for int
if age:
    age = int
    # 18-21 wristband
    if age >= 21:
        print("You are good to enter, and are able to drink.")
    # 21+ drink, normal entry
    elif age >= 18:
        print("You can enter, but need a wristband!")
    # too young, sorry
    else:
        print("You are not old enough to come in.")
else:
    print("Please enter an age.")
```

### Exercise

```python
# NO TOUCHING==NO TOUCHING==NO TOUCHING==NO TOUCHING #| \
from random import randint                           #|  \
x = randint(-100, 100)                               #|   \
while x == 0:  # make sure x isn't zero              #|    \
    x = randint(-100, 100)                           #|     NO TOUCHING!!!!!! (please)         
y = randint(-100, 100)                               #|    /
while y == 0:  # make sure y isn't zero              #|   /
    y = randint(-100, 100)                           #|  /
# NO TOUCHING==NO TOUCHING==NO TOUCHING==NO TOUCHING #| /



# Don't change the print statements so the tests can pass!
# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
if x > 0 and y > 0:
    print("both positive")
elif x < 0 and y < 0:
    print("both negative")
elif x > 0 and y < 0:
    print("x is positive and y is negative")
else:
    print("y is positive and x is negative")

# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```

:heavy_check_mark: **Well done, your solution is correct!**

```python
# NO TOUCHING ======================================

from random import choice, randint

# randomly assigns values to these four variables
actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)

# NO TOUCHING ======================================


calling_in_sick = None  # set this to True or False with Boolean Logic and Conditionals!

# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

if actually_sick and sick_days > 0:
    calling_in_sick = True
elif kinda_sick and hate_your_job and sick_days > 0:
    calling_in_sick = True
else:
    calling_in_sick = False

# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

:heavy_check_mark: **Well done, your solution is correct!**


