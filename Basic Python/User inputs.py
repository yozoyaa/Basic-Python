# ------------------------------------------------
# EXERCISE 1 MAD LIBS
# ------------------------------------------------
adjective1 = input("Enter an adjective: ")
noun = input("Enter a noun: ")
adjective2 = input("Enter an adjective: ")
verb = input("Enter a verb: ")
adjective3 = input("Enter an adjective: ")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw {noun}.")
print(f"{noun} was {adjective2} and {verb}ing.")
print(f"I was {adjective3}!")

# ------------------------------------------------
# EXERCISE 2 AREA CALC
# ------------------------------------------------
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

# area = length * width
# print(f"The area is: {area}cm^2")

# ------------------------------------------------
# EXERCISE 3 SHOPPING CART
# ------------------------------------------------
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${round(total, 2)}")