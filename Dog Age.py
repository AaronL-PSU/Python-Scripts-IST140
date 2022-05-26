dogage=int(input("Enter your dog's age: "))
if dogage<2:
    humanage = dogage*10.5
    print("Your dog is " + str(humanage) + " years old.")
elif dogage>2:
    humanage=21+((dogage-2)*4)
    print("Your dog is " + str(humanage) + " years old.")
