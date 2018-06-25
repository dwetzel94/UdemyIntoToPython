#pound sign makes a comment
#strings can take either single or double parenthesis
# greeting = "hello"
# name = input("Please enter your name \n")
# print(greeting + ' ' + name)

#back slash: \
splitString = "This string has been \nsplit over \n3 lines"
print(splitString)

#\n= line break, \t= tab
tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

print('The pet shop owner said "No, no, \'e\'s ...he\'s resting"')

anotherSplitString = """This string has been 
split over
several lines"""
print(anotherSplitString)

_myName_ = "Demi"
#variable names are case sensitive
#print() with + only works with multiples of the same variable type

age = 24

#basic calculations
a = 12 #int
b = 3
print(a + b)
print(a / b) #returns a float because python automatically gives a decimal answer when dividing
print(a // b) #// returns integer value when dividing
print(a % b) #% gives remainder value if the numbers were divided

#strings- sequence data type of characters
parrot = "Norwegian Blue"
print(parrot[3])  #treat string like an array, printing one element
print(parrot[-1])  #starting at end of string
print(parrot[0:6])  #printing a range
print(parrot[-4:-2])
print(parrot[0:6:2])  #extract characters from 0 to 6, taking every second character
print(parrot[0::3])  #extract characters from 0 onward, taking every third character

#string operators
print("Hello\n" * 5)
today = "monday"
print("day" in today)  #gives true or false