import random

NUMBER = random.randint(1, 100)

print("Welcome to Number Guessing Game!~")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard'.").lower()
if difficulty == "easy":
    attempt = 10
elif difficulty == "hard":
    attempt = 5


def guessing_game():
    for tries in range(attempt, 0, -1):
        print(f"You have {tries} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))
        if guess == NUMBER:
            print(f"You got it! The answer is {NUMBER}.")
            return
        elif guess > NUMBER:
            print("Too high.")
        elif guess < NUMBER:
            print("Too low")
        if tries - 1 == 0:
            print(f"You've run out of guesses. The number was {NUMBER}")
        else:
            print("Guess again.")

guessing_game()


