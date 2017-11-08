# Creating a simple computer (guessing) game.
# 6 November, 2017
# CTI-110 M6HW2 - Random Number Guessing Game
# Manuel Maldonado

# A basic computer game that asks the user to guess the "Secret" random number.

# Import Module
import random

def main():

    # Call play_game() here, then ask user to enter y and loop back.
    play_game()

    # After first playthrough, ask if again?
    again = input("Do you want to play again? (y / n)")
    print("")

    # Loop to continue asking if again after first play.
    while again == 'y' or again =='Y':
        play_game()
        print("Do you want to play again? (y / n)")
        print("")
        again = input()

    # Close loop (program).
    print("Thanks for Playing, Good Bye!")

# Define the game.
def play_game():

    # Should contain game itself, generate number here then loop until correct guess.

    # Constant to limit gameplay. *Bonus
    guessesTaken = 0

    # Introduction to game.
    print("Hello I want to play a game, can you guess the secret number?")
    print("Here's a hint, it is between 1 and 100.")
    print("The catch is, you must guess correctly within 7 tries.")
    print("Good Luck!")
    print("")

    # Create the Secret Number.
    secretNumber = random.randint(1, 100)

    # Constant for while loop (Game).
    letsPlay = True

    # Loop for game.
    while letsPlay:

        # Ask user for input (Guesses).
        guess = int(input("What's your guess? "))

        # Guess counter *Bonus
        guessesTaken = guessesTaken + 1

        # End game if over 7 guesses. *Bonus
        if guessesTaken >= 7:
            letsPlay = False
            print("GAME OVER")
            print("")

        # Too high
        elif guess > secretNumber:
            print("That guess is too high, try again.")
            print("")
            
        # Too low          
        elif guess < secretNumber:
            print("That guess is too low, try again.")
            print("")

        # Guess correctly, game ends.
        else:
            if guess == secretNumber:
                print("Nice you guessed correctly, someone's a Genius!")
                print("")
                letsPlay = False

    # Print guesses taken. *Bonus          
    print("You guessed", guessesTaken, "times.")
    print("")

# Start the program.
main()

# Bonus tell user how many guesses it took after they guess correct

# Bonus 2 limit the game to a certain amount of guesses (a fair amount)
