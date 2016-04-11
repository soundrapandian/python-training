# Think of a number between 0 and 99. Then write a python program
# to guess the number you have thought of
import random


print ("I have guessed a number")

min_range = 0
max_range = 99
guess = random.randint(min_range, max_range)

while True:
    answer = input("Is it {} [(y)es/(h)igher/(l)ower]:".format(guess))
    if answer == "y":
        break
    elif answer == "l":
        min_range = guess + 1
        guess = random.randint(min_range, max_range)
    elif answer == "h":
        max_range = guess - 1
        guess = random.randint(min_range, max_range)
    else:
        print ("Allowed answers are - y, h, l")
print ("Done!")