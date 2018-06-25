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

#variable names are case sensitive
#print() with + only works with multiples of the same variable type

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

#string formatting
age = 24
print("My age is " + str(age) + " years")

#replacement fields
print("My age is {0} years".format(age))
print("There are {0} days in {1}, {2}, {3} and {4}".format(30,
    "April", "June", "September", "November"))

print("January: {2}, February: {0}, March: {2}, April: {1}".format(28, 30, 31))

print("My age is %d years" % age)  #% is an old syntax for string formatting from python 2
print("My age is %d %s, %d %s" % (age, "years", 6, "months"))  #d= integer, s = string

#for loop
for i in range(1, 12):
    print("number %2d squared is %4d and cubed is %4d" %(i, i ** 2, i ** 3))
    #number in front if % is for spacing; ** indicates exponents

print("Pi is approximately %12.50f" % (22 / 7))

#python 3 replacement fields with spaccing formatting
for i in range(1,12):
    print("Number {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))
    # {replacement field number : width} <: left justification