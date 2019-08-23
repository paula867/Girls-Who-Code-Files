import random

# A list of words that 
potential_words = ["jazz"] #, "rogue", "fishhook", "hyphen", "awkward","ivory","polka", "pixel", "zombie"

word = random.choice(potential_words)

# Use to test your code:
#print(word)

# Converts the word to lowercase
current_word = ["_", "_"] # TIP: the number of letters should match the word
word = word.lower()
i=2
while i < len(word):
    current_word.append("_")
    i += 1



# Some useful variables
guesses = []
maxfails = 7
fails = 0

while fails < maxfails:
    print(current_word)
    guess = input("Guess a letter: ")
    guesses.append(guess)
    
	# check if the guess is valid: Is it one letter? Have they already guessed it?

	# check if the guess is correct: Is it in the word? If so, reveal the letters!

	fails = fails+1
	print("You have " + str(maxfails - fails) + " tries left!")
    
    if(guess.isalpha() == false):
        print("That is not a letter. Please try again.")
        quess = input("Guess a letter: ")
    else:
        if(guess in word):
            print("You got a letter!")
            print("Guess a letter: ", guess)
            potential_words[i]
            print([i])
        else:
            print("You guessed wrong!")
            fails = fails+1
            print("You have " + str(maxfails - fails) + " tries left!")
