import random

def number_guess():

#FIRST LOOP THAT COVERS WHOLE GAME
    while True:
        number = random.randint(1, 100)
        print("I have guessed a number between 1 and 100. Can you guess it?")
        attempts = 0

# LOOP THAT COVERS LOGIC OF GAME
        while True:
            guess = int(input("Enter your number (1-100): "))
            attempts += 1

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number correctly in {attempts} attempts.")
                break  # Exit

# Ask if the user wants to play again
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != "y":
            print("Thanks for playing! Have a nice day! 😊")
            break  # Exit

number_guess()
