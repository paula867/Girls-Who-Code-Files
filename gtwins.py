import random

# A list of words that 
potential_words = ["example", "words", "someone", "can", "guess"]

word = random.choice(potential_words)

#Use to test your code:
#print(word)

#Converts the word to lowercase
word = word.lower()

#Make it a list of letters for someone to guess
current_word = ["_", "_"] #TIP: the number of letters should match the word
i = 2
while i < len(word):
    current_word.append("_")
    i += 1

#Some useful variables
guesses = []
maxfails = 7
fails = 0

while fails < maxfails:
    guess = input("Guess a letter: ")

	# check if the guess is valid: Is it one letter? Have they already guessed it?
    if(guess.isalpha() == False):
        print("The character you have entered is not valid. Guess again.")
    elif(len(guess) != 1 ):
        print("Please enter only once character at a time. Guess again.")
    elif(guess in guesses):
        print("The character you have entered has already been guessed. Guess again.")
    else: 
	# check if the guess is correct: Is it in the word? If so, reveal the letters!
        guesses.append(guess)
        if(guess in word):
            #revealing the letter in current_word in correct  (find index of the letter[guess] in word[variable])
            #the text above means that you have to loop[index] through word[the variable] to see if guess in word.
            #{word = "lemon" 
            #word[0] = guess?
            #word[1] = guess? so on...
            #current_word[in] = guess}
            # = to set something to something*****
            # == is a boolean used to compare two things*****
            for indx in range(len(word)): 
                if(word[indx] == guess): #so if the guess is in word then 
                    current_word[indx] = guess #if you find the guess in index then change it with guess
            print("You guessed right!")
        else:
            #say your wrong
            #append guess to guesses
            print("You guessed wrong, try again!")
            fails = fails+1
    print(current_word)
    print("Quesses: ", guesses)
    print("You have " + str(maxfails - fails) + " tries left!")
    print("----------------------------------------")
    #check if there are any letters to quess
    
