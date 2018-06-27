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


# Program Flow Challenge 1

# Create a program that takes an IP address entered from the keyboard and prints out the number
# of segments it contains and the length of each segment. IP addresses contain 4 numbers with stops
# in between but the program should also work with invalid IP addresses.

IPaddress = input("Please enter the IP address.\n")
segment = 1
segmentLength = 0
character = ""

for character in IPaddress:
    if character == '.':
        print("segment {0} contains {1} characters".format(segment, segmentLength))
        segment += 1
        segmentLength = 0
    else:
        segmentLength += 1
    # last segment does not get printed unless the final character is a '.'

if character != '.':
    print("segment {0} contains {1} characters".format(segment, segmentLength))

