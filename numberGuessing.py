import random
secret = random.randint(1, 100)
attempts = 0
game=True

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while game:
    guess = int(input("Make a guess: "))
    if guess < secret:
        attempts += 1
        print("Too low.")
    elif guess > secret:
        attempts += 1
        print("Too high.")
    elif guess == secret:
        attempts += 1
        print(f"Congratulations! You've guessed the number {secret} in {attempts} attempts.")
        game=False
        break
    else:
        print("Invalid input. Please enter a number between 1 and 100.")


