import random

# A list of words that 
potential_words = ["jazz"] #, "rogue", "fishhook", "hyphen", "awkward","ivory","polka", "pixel", "zombie"

word = random.choice(potential_words)

# Use to test your code:
print(word)

# Converts the word to lowercase
word = word.lower()
i=2
while i < len(word)
    current_word = current_word.append("_")
    i += 1
current_word = ["_", "_"] # TIP: the number of letters should match the word
if(len(word) == 3):
    print(current_word[0])

# Some useful variables
guesses = []
maxfails = 7
fails = 0

while fails < maxfails:
	guess = input("Guess a letter: ")

	# check if the guess is valid: Is it one letter? Have they already guessed it?

	# check if the guess is correct: Is it in the word? If so, reveal the letters!

	print(current_word)

	fails = fails+1
	print("You have " + str(maxfails - fails) + " tries left!")
