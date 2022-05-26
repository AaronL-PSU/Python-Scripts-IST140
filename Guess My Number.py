import random
number = (random.randint(1,100))
guess=int(input("I have chosen a number between 1 and 100. What is my number?: "))
count = 0
while count<10:
    if guess<number:
        guess=int(input("Too low! Guess again: "));
        count+=1
    elif guess>number:
        guess=int(input("Too high! Guess again: "))
        count+=1
    elif guess==number:
        print(str(number) + " was my number! You win!")
        break
if count==10:
    print("You ran out of guesses. The number was: " + str(number))
