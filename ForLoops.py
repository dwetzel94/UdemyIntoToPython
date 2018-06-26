#len= funtion that calls the length of a string
#[] indicates position within the string

# number = "9,223,372,036,854,807"
# cleanedNumber = " "
#
# for char in number:
#     if char in '0123456789':
#         cleanedNumber = cleanedNumber + char
#
# newNumber = int(cleanedNumber)
# print("The Number is {}".format(newNumber))
#
# for state in ["not pining", "no more", "a stiff", "bereft of life"]: #array of strings
#     print("This parrot is " + state)
#     # equivalent to print("This parrot is {}".format(state))
#
# for i in range(0, 100, 5): #third value is a STEP between values
#     print(i)
#
# #nested loop
# for i in range(1, 13):
#     for j in range(1,13):
#         print("{1} times {0} is {2}".format(i, j, i*j))
#     print("===============")

#Extracting capitals exercise
quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
capital = ""
for char in quote:
    if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        capital = capital + char

newString = capital
print(newString)

#step exercise- print numbers divisible by 7 from 0 to 100
for i in range(0, 100, 7):
    print(i)