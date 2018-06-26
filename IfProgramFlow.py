age = int(input("How old are you?\n"))
if not(age<18):
    print("You can vote")
else:
    print("please come back in {} years".format(18 - age))