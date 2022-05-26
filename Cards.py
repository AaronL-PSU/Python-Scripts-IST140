#Create a program that will display 4 random cards (without replacement) from a full deck of cards
#•You have to use lists:
#•1 list for the suite
#•1 list for the individual cards
#•1 list for the deck
#•If you want you can use random.shuffle(list) method, but you don’t have to!
import random
suit=["Clubs","Diamonds","Hearts","Spades"]
card=["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
deck=[]
n=0
while n<4:
    random.shuffle(suit)
    random.shuffle(card)

    x=suit[0]
    y=card[0]
    
    if(deck.count(str(y + " of " + x)) == 0):
        deck.append(str(y + " of " + x))
        n=n+1

print(deck)
