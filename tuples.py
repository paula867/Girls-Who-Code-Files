print(" ")
print("The function of tuples is to make lists.")
print("With tuples you cannot write any code to modify the tuple but with lists you can.")
print(" ")
print("Tuples are like lists but can't be changed.")
print(" ")
print("Instead of using square brackets they use paretheses.")
print("Always include a comma after a tuple even if there is only one value.")
print("The indices of tuples also start with 0 like in lists.")
print(" ")
print("With tuples you can use ratios to display certain indices.")
numbers = [6,7,8,9,10]
names = ["Gabriela", "Angie", "Auriel", "Paula"]
names[0] = "Gabi"
tup1 = (0,1,2,3,4,5)
tup2 = ("science","technology","math","art and design","biology") 
print("If you wanted to change the indice of a list you could by setting something to the indice of the list.")
print(" ")
print("For example: if you were to make a list 'letters = [a,b,c,d]' and then you set indice 0 to be m 'letter[0] = m'")
print("The python interpreter will have no problem making this change.")
print("But with a tuple, you can't do this. If you try to set an indice to be something")
print("different by coding 'letter[0] = m' the interpreter will give you an error.")


print(tup2[1])
print(tup1[0:3])
print(tup1 + tup2)
print(names + numbers)
tup3 = tup1 + tup2
list3 = names + numbers
print(tup3)
print(list3)
tup2[2] = "mathematics"



