from ramdom import *

aRamdomNumber = randint(1, 20)
print(aRamdomNumber)

guess = input("Quess a number between 1 and 20 (inclusive): ")
if not guess.isnumeric():
    print("That's not a positive whole number, try again!")
else: #what this is saying is that if the number is between 1 and 20 it will perform the following. 
    guess = int(guess)#convert to integer #indents are important, see how the else loop is the first indent. 
    #The while loop is the second loop. The if and then are the third loops 
    #and prints and breaks are the fourth loops. 
    i = 0 #sets the variable for the amount of times you can repeat the guess
    while i < 2: #sets loop
        if (guess == aRandomNumber):
            print("You got the number")
            break
    else: # tells you that is the guess is not equal to the ramdom number
        if(guess < aRamdomNumber):
            print("Go higher.")
        else: # you don't need a if(guess > aRamdomNumber): because only two things can happen. 
            print("Go lower.")
    guess = int(input("Try again")) #reloop
    i += 1 #changes i to make sure the loop breaks after 3 tries.
   
    print("the number was", aRamdomNumber) #tells the player they lost. 


