

answer = input("what is 2+1? ")

while True:
    if(answer != "3"):
        print("Incorrect. Try again!")
        answer = input("What is 2+1? ")
    else:
        print("Correct! You can move on")
        print("Please answer with the letter option only for the next question.")
        answer2 = input("Second question: which a prokaryotic? Option A: a cell with no nucleus. Option B: A cell with a nucleus. ")        
        if(answer2 == "A" or "a"): 
            print("Correct!")
            answer3= input("what is the third letter of the alphabet? ")
            if (answer3 == "C" or "c"):
                print("Correct! You won the game!")
                break
            elif(answer3 != "C" or "c"):
                print("Incorrect, try again.")
        else:
            print("Wrong try again.")