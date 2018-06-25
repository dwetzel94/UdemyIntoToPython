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
b = 3.5
print(a + b)
print(a / b) #returns a float because python automatically gives a decimal answer when dividing
print(a // b) #// returns integer value when dividing
print(a % b) #% gives remainder value if the numbers were divided
