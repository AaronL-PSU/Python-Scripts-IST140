from math import ceil #Inputs ceiling function from the Math library
try: #Checks if input is a float
    h = float(input ("Height in feet: "))
    w = float(input ("Width in feet: "))
    l = float(input ("Length in feet: "))
except ValueError: #If input is not a float, an exception is thrown
    print("Input must be a number.")
    input('Press ENTER to exit and try again') #Stops program from closing until there is a user input
sqft = (2*w*h+2*l*h)
gal = (ceil(sqft/400)) #Uses ceiling function to round up
print ("Your walls are " +str(sqft) + " square feet.")
print ("You will need " +str(gal) + " gallons of paint.")
input('Press ENTER to exit') #Stops program from closing until there is a user input
