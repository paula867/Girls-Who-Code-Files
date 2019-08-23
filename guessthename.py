from ramdom import *

aRamdomNumber = randint(1, 20)
print(aRamdomNumber)
guess = input("Quess a number between 1 and 20 (inclusive): ")
if not guess.isnumeric():
    print("That's not a positive whole number, try again!")
else:
    guess = int(guess)
i = 0
   
if(guess == aRamdomNumber):
            break
                print("You are correct!!")
                
if(guess < aRamdomNumber):
            print("Guess higher.")
    
    else: guess > aRamdomNumber
            print("Guess lower.")
    
            i += 1
        
