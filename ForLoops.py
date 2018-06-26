# for i in range(1,20):
#     print("i is now {}".format(i + 1))
#
# number = "9,223,372,854,775,807"
# for i in range(0, len(number)): #len= funtion that calls the length of a string
#     print(number[i]) #[] indicates position within the string

number = "9,223,372,854,775,807"
for i in range(0, len(number)):
    if number[i] in "0123456789": #skips commas
        print(number[i], end= '')