age = 7

# 2-8 2 dollar ticket
# 65+ 5 dollar ticket
# 10 dallar ticket

if not ((age >= 2 and age <= 8) or age >= 65):
    print("You pay $10 and are not a child or senior.")
else:
    print("You are a child or senior.")