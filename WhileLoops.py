# for i in range(10):
#     print("i is not {}".format(i))
#
# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1
#
# availableExits = ["east", "north east", "south"]
# chosenExit = ""
#
# while chosenExit not in availableExits:
#     chosenExit = input("Please choose a direction: ")
#     # application: reading data from a file
#     if chosenExit == "quit":
#         print("Game over")
#         break
#
# else:
#     print("You got out of there")
#
#

# Challenge: generate random number and make a guessing game for that number

import random

highest = int(input("Enter the highest number you'd like to guess from: "))
NumberOfGuesses = int(input("How many guesses do you want? "))
print("Okay, now guess a number between 1 and {}. You have {} guesses.".format(highest, NumberOfGuesses))
print("Enter 0 as your guess to exit the game.")
answer = random.randint(1, highest)

i = 1
while i <= NumberOfGuesses:
    guess = int(input())
    if guess == 0:
        print("Ok. Game over. The number was {}".format(answer))
        break
    if i == NumberOfGuesses and guess != answer:
        print("Nope. That was your last guess. The answer was {}".format(answer))
        break
    if guess != answer:
        if guess > highest:
            print("You guessed beyond the highest value. Try again.")
            continue
        if guess < answer:
            print("Oops, too low. Guess higher.\n")
        if guess > answer:
            print("Too high, please guess lower.\n")
    else:
        print("Good job! You matched the right number of {}.".format(answer))
        break
    i += 1


if i > NumberOfGuesses:
    print("You ran out of guesses. The correct number was {}".format(answer))