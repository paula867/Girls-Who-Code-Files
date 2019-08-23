import random
# --- Define your functions below! ---
def intro():
    print("Hi my name is Lemon. Let's talk.")
    print("Type something and hit enter. ")
   
    
#def process_input(answer): #what this is saying is that it will process the a given variable when called
    
    #if(answer == "Hello"): #here you are saying answet needs to be equal to Hello for you to say Hi back. 
        #say_greeting()
    #else:
        #say_name() #if you see the empty parenthesis it's most likely a function.
        
def say_greeting():
    print("Hi")
    
def say_name(): #the parentheses is the parameter
    print("Nice to meet you! My name is Paula.")
    
def is_itvalid(response, valid_responses):
    if(response in valid_responses):
        return True
    return False
    
def isitvalid_game(answer, rpc, rchoice):
    if(answer in rpc):
        return True
    return False
    


def findoutcome(answer, rpc, rchoice):
    if(rchoice == "rock"):
        if(answer == "scissors"):
            print("You lost!")
        elif(answer == "rock"):
            print("It's a tie!")
        elif(answer == "paper"):
            print("You won!")
    elif(rchoice == "paper"):
        if(answer == "rock"):
            print("You lost!")
        elif( answer == "paper"):
            print("It's a tie!")
        elif(answer == "scissors"):
            print("You won!")
    elif(rchoice == "scissors"):
        if(answer == "paper"):
            print("You lost!")
        elif(answer == "rock"):
            print("You won!")
        elif(answer == "scissors"):
            print("It's a tie!")

   


# --- Put your main program below! ---
def main():
    intro()
    while True:
        rpc = ["rock", "paper", "scissors"]
        rchoice = random.choice(rpc)
        valid_responses = ["Hello", "hello", "Hi", "hi", "What's good", "What's good?", "what's good", "what's up", "What's up", "Hey", "hey"]
        response = input("Hi there! ") #you are setting the variable response
        if(is_itvalid(response, valid_responses)):
            game = input("Do you want to play rock paper scissors? ")
            if(game == "yes"):
                print("Rock, Paper, Scissors...")
                user_rpc = input("GO!  ")
                user_rpc = user_rpc.lower()
                if(isitvalid_game(user_rpc, rpc, rchoice)):
                    print(rchoice)
                    findoutcome(user_rpc, rpc, rchoice)
                    break
            else: 
                print("Okay, have a nice day!")
                break
        else:
            print("Have a nice day! Goodbye!")
            break





# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()