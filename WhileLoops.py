for i in range(10):
    print("i is not {}".format(i))

i = 0
while i < 10:
    print("i is now {}".format(i))
    i += 1

availableExits = ["east", "north east", "south"]
chosenExit = ""

while chosenExit not in availableExits:
    chosenExit = input("Please choose a direction: ")
    # application: reading data from a file
    if chosenExit == "quit":
        print("Game over")
        break

else:
    print("You got out of there")


