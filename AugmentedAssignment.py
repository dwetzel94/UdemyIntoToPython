

number = "9,223,372,036,854,755,807"
cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber += number[i]  # augmented assignment

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))

x = 23
x += 1  # equivalent to x = x + 4
print(x)

x*=2
print(x)

#strings
greeting = "good"
greeting += "morning"
print(greeting)

greeting *= 5
print(greeting)

