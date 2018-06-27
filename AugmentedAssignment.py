

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

# strings
greeting = "good"
greeting += "morning"
print(greeting)

greeting *= 5
print(greeting)

# AA exercise
number = 7
multiplier = 7
answer = 0

# number += (multiplier-1)*number
# print(number)

for i in range(0, multiplier):
    if i != (multiplier - 1):
        continue
    else:
        number += i*number
        answer = number
print(answer)

# OR
for i in range(multiplier):
    answer += number
print(answer)