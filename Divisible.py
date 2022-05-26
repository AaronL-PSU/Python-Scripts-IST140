num1 = (int(input("Number 1: ")))
num2 = (int(input("Number 2: ")))
try:
    r = (num1 % num2)
except ZeroDivisionError:
    print("You cannot divide by zero!")
    input("Press ENTER to exit")
if r == 0:
    print("They are divisible")
else:
    print("They are not divisible")
input("Press ENTER to exit")
