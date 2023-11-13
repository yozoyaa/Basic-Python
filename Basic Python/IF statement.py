# if = Do some code IF condition is True
# else = Do something else if above condition/s are False

# —---------------------
#   EXAMPLE 1
# —---------------------
age = int(input("Enter your age: "))

if age >= 100:
   print("You are too old to sign up")
elif age >= 18:
   print("You are now signed up")
elif age < 0:
   print("You haven't been born yet")
else:
   print("You must be 18+ sign up")

# —---------------------
#   EXAMPLE 2
# —---------------------
response = input("Do you want food (Y/N)?: ")

if response == "Y":
   print("Have some food")
else:
   print("No food for you!")

# —---------------------
#   EXAMPLE 3
# —---------------------
name = input("Enter your name: ")

if name == "":
   print("You did not enter your name!")
else:
   print(f"Hello {name}")

# —---------------------
#   EXAMPLE 4
# —---------------------
online = False

if online :
   print("You are online")
else:
   print("You are offline")