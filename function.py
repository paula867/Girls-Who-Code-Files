import random
# --- Define your functions below! ---
def intro():
    print("Hi my name is Lemon. Let's talk.")
    print("Type something and hit enter. ")
   
    
def process_input(answer): #what this is saying is that it will process the a given variable when called
    
    if(answer == "Hello"): #here you are saying answet needs to be equal to Hello for you to say Hi back. 
        say_greeting()
    else:
        say_name() #if you see the empty parenthesis it's most likely a function.
        
def say_greeting():
    print("Hi")
    
def say_name(): #the parentheses is the parameter
    print("Nice to meet you! My name is Paula.")
    
rpc = ["rock", "paper", "scissors"]
rpc = rpc.lower()

rchoice = random.choice(rpc)

def findanswer(answer)
    if(rchoice = "rock"):
        user_rpc != "paper" or "rock"
        print("You lost!")
        elif(user_rpc == "rock"):
            print("It's a tie!")

   


# --- Put your main program below! ---
def main():
    intro()
    while True:
        response = input("(What will you say?) ") #you are setting the variable response
        process_input(response) #you are calling the variable process_input to process response for answer 
        game = input("Do you want to play rock paper scissors?")
        if(game == "Yes" or "yes"):
            print("Please write your answer 
            print("Rock, Paper, Scissors...")
            user_rpc = input("GO! ")
            findanswer(user_rpc)
        else:
            print("Have a nice day! Goodbye!")
            break





# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()