#len= funtion that calls the length of a string
#[] indicates position within the string

number = "9,223,372,036,854,807"
cleanedNumber = " "

for char in number:
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char

newNumber = int(cleanedNumber)
print("The Number is {}".format(newNumber))

for state in ["not pining", "no more", "a stiff", "bereft of life"]: #array of strings
    print("This parrot is " + state)
    # equivalent to print("This parrot is {}".format(state))

for i in range(0, 100, 5): #third value is a STEP between values
    print(i)