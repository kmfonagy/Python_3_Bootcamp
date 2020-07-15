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