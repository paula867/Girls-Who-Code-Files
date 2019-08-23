#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")

print("Can your password survive a dictionary attack?")

def variation_test(test_password):
    test_password = test_password.replace("4","a")
    test_password = test_password.replace("$","s")
    test_password = test_password.replace("0","o")
    test_password = test_password.replace("@","a")
    test_password = test_password.replace("3","e")
    test_password = test_password.replace("1","i")
    test_password = test_password.replace("5","s")
    test_password = test_password.replace("2","z")
    test_password = test_password.replace("9","q")
    test_password = test_password.replace("6","b")
    return test_password

#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
test_password = input("Type in a trial password: ")

#Write logic to see if the password is in the dictionary file below here:

for p in f:
    if(test_password.strip() == p.strip()): #strip cuts all the spaces. Do this when you use txt files.
        print("Your password is in our data file. That means your password is NOT SECURE.", test_password)
        break
    elif(variation_test(test_password) == p.strip()):
        print("Your password is BAD.", test_password)
        break
    else:
        continue 
    print("Your password is NOT in out data base.")
