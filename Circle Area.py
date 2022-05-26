from math import pi #Inputs exact value of pi from the Math library
try: #Checks if input is a float
    r = float(input ("Radius: "))
except ValueError: #If input is not a float, an exception is thrown
    print("Input must be a number.")
    input('Press ENTER to exit and try again') #Stops program from closing until there is a user input
print ("Decimal Area = " +str(pi*r*r) + " u².")
print ("Area in terms of pi = " +str(r*r) + "π " + " u².") #Area in terms of pi is exact
input ("Press ENTER to exit") #Stops program from closing until there is a user input
