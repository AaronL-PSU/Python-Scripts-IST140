yr = int(input ("Year: "))
if yr % 4 == 0:
    print("This is a leap year")
elif yr % 100 == 0:
    print("This is not a leap year")
elif yr % 400 == 0:
    print("This is a leap year")
else:
    print("This is not a leap year")
