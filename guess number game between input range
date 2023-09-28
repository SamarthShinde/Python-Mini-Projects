import random

def number_guesser(lower_limit, upper_limit):
    secret_number = random.randint(lower_limit, upper_limit)
    attempts = 0

    print(f"Welcome to the Number Guesser Game!")
    print(f"I have selected a random number between {lower_limit} and {upper_limit}. Try to guess it!")

    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < secret_number:
            print("Too low! Try again.")
        elif user_guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

lower_no=int(input("enter a lower range starting number : "))
upper_no=int(input("enter the higher range upper number: "))
number_guesser(lower_no,upper_no)
