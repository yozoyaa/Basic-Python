# logical operators = used on conditional statements

#              and = checks two or more conditions are True
#               or = checks if at least one condition is True
#              not = True if condition is False, and vice versa

temp = 20
sunny = True

if temp <= 0 or temp >= 30:
    print("The temperature is bad")
else:
    print("The temperature is good")

if not sunny:
    print("It is cloudy")
else:
    print("It is sunny")