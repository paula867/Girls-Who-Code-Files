import json
import statistics

questions = ["What is your name?",
             "What is your favorite color?",
             "What town and state do you live in?",
             "What is your age?",
             "What year were you born?"]
answers = {}
keys = ["Name", "Favorite color", "Hometown","Age", "Birthyear"]
all_answers = []

choice = input("Would you like to take a survey? Type yes or no.    ")
while choice == "yes": #forever loop
    answers = {} # this dictionary used to be outside. The answers would be replaced everytime someone took a survey with the answers of the last survey. 
    # When answers was put inside the while loop, that didn't happen anymore. 
    for q in range(len(questions)): #when you use for i in range i = to an interger. When you use for i in list i = to a concept or variable. 
        response = input(questions[q] +"   ") # raw_input is the same as input for now 
        answers[keys[q]] = response #sets the keys(list) to a value every time you go through the loop
        
    all_answers.append(answers)
    choice = input("Would you like to take a survey? Type yes or no.    ")
    
json_file = open("json.json", "w")
index = 0

json_file.write('[\n')
for d in all_answers: 
    if (index < len(all_answers) - 1): #length is always one more than the index
        json.dump(d,json_file) #opening json file then storing all the items (dictionaries/ d) in all_answers
        json_file.write(',\n') #writes into json file #'\n' adds a new line or what is known as 'enter' for humans
    else: #will be the last index because the index is less than the length not less than or equal to. 
        json.dump(d, json_file)
        json_file.write('\n')
    index += 1
    
json_file.write(']') # .write adds things to a json file.
json_file.close() #closes json file

ages_surveys = []
for a in all_answers:
    the_ages = a["Age"] #add the age you find in all_answers to the_ages
    the_ages = int(the_ages)
    ages_surveys.append(the_ages)
    
cities = []
for c in all_answers:
    city = c["Hometown"]
    cities.append(city)
    

colors = []
for o in all_answers:
    color = o["Favorite color"]
    colors.append(color)


print(all_answers)
print("The average age of the participants is", statistics.mean(ages_surveys))
print("The city most people live in is ", statistics.mode(cities))
print("The most liked color among the participants is", statistics.mode(colors))
