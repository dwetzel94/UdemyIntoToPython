# parrot = "Norwegian blue"
#
# letter = input("Enter a character: ")
#
# if letter in parrot: #'in' looks for the condition within the parameter
#     print("Give me a {}, nibba".format(letter))
# else:
#     print("I don't need that letter")

#simple condition challenge
# x = 7
# y = 7
#
# if x > y:
#     print("x is greater than y")
# elif x < y:
#     print("x is smaller than y")
# else:
#     print("x is equal to y")

#Challenge 1:
# Write a small program to ask for a name and an age.
# When both values have been entered, check if the person if the right age
# to go on a 18-30 holiday. if they are, welcome them to the holiday, otherwise
# print a polite message refusing entry.

name = input("Hello there, what is your name?\n")
age = int(input("Nice to meet you, {}! How old are you?\n".format(name)))

if 18 < age < 31:
    print("Ah yes, since you are at the prime age of {}, you may come on holiday with us. Welcome!\n".format(age))
else:
    print("I'm sorry, but since you are {}, you cannot come along for the holiday.".format(age))