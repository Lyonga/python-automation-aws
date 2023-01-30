from random import randint

while True:
    number_to_guess = randint(1, 19)
    users_guess = int(input("Guess the number: "))

    if users_guess == number_to_guess:
        print("YOU WON!")
        break

    elif users_guess < number_to_guess:
        print("You guessed too low")

    elif users_guess > number_to_guess:
        print("You guessed too high")

