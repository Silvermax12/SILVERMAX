print("Silvermax Welcomes You")
# program for the computer make guess within a specified range
import random
def computer_guess(lower_bound, upper_bound):
    return random.randint(lower_bound, upper_bound)
# so this is the main program for the guessing game
def max():
# So this is where the user will input the numer range
    small= int(input("Enter the smallest number u can think of: "))
    large = int(input("Enter the largest number u can think of: "))
    print("Think of a number between the range of two numbers and I will guess it.")
    count = 0
    lower_bound = small
    upper_bound = large
    # below we have the loop for the number guessing
    while True:
        count += 1
        guess = computer_guess(lower_bound, upper_bound)
        print(f"My guess is: {guess}")
        response = input("Is my guess correct? (yes/no): ").lower()
        if response == "yes":
            print(f"I guessed your number in {count} guesses. Your Mind Is Predictable.")
            print("I thought u were smarter than this")
            break
        elif response == "no":
            help = input("Is the number higher or lower than my guess? And be more specific please: ").lower()
            if help == "higher":
                lower_bound = guess + 1
            elif help == "lower":
                upper_bound = guess - 1
            else:
                print("Please enter 'higher' or 'lower'.")
        else:
            print("Please enter 'yes' or 'no'.")

max()
print("All Hail Silvermax")
