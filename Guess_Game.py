import random

guess = random.randint(1, 100)
no_of_guesses = 0

while (1):
    your_guess = int(input("Your Guess:"))
    if your_guess > guess:
        print("lower number please")
        no_of_guesses += 1
        continue
    elif your_guess < guess:
        print("higher number please")
        no_of_guesses += 1
        continue
    else:
        no_of_guesses += 1
        print(f"number of gueses:{no_of_guesses}")
        break
