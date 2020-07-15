print("How many kilometers did you run today?")
kms = float(input())
miles = kms/1.60934
miles = round(miles, 2)
print(f"\nYour {kms} km run is equal to {miles} mi!\n")