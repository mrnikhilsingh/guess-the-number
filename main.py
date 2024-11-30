import random  # Import the random module for generating the secret number

def game_setup():
    """
    Set up the game by allowing the player to choose a difficulty level 
    and generating the secret number.
    Returns: 
        difficulty (int): The chosen difficulty level.
        max_attempts (int or None): The maximum number of attempts allowed, or None for unlimited.
        secret_number (int): The randomly generated secret number.
        range_start (int): The start of the range for the secret number.
        range_end (int): The end of the range for the secret number.
    """
    print("Welcome to the Enhanced Number Guessing Game!")
    print("Choose a difficulty level:")
    print("1. Easy (Unlimited attempts)")
    print("2. Medium (10 attempts)")
    print("3. Hard (5 attempts)")
    
    while True:
        try:
            # Ask the player to select a difficulty level
            difficulty = int(input("Enter your choice (1/2/3): "))
            if difficulty not in [1, 2, 3]:
                print("Please choose a valid option (1, 2, or 3)!")
                continue
            break
        except ValueError:
            # Handle non-numeric input
            print("Invalid input! Please enter a number (1, 2, or 3).")

    # Determine maximum attempts based on the chosen difficulty level
    max_attempts = None if difficulty == 1 else (10 if difficulty == 2 else 5)
    range_start, range_end = 1, 100  # Define the range for the secret number

    # Generate the secret number randomly within the range
    secret_number = random.randint(range_start, range_end)
    return difficulty, max_attempts, secret_number, range_start, range_end

def play_game(difficulty, max_attempts, secret_number, range_start, range_end):
    """
    Handles the main gameplay loop where the player guesses the number.
    Parameters:
        difficulty (int): The chosen difficulty level.
        max_attempts (int or None): Maximum attempts allowed, or None for unlimited.
        secret_number (int): The randomly generated secret number.
        range_start (int): The start of the range for the secret number.
        range_end (int): The end of the range for the secret number.
    Returns:
        score (int): The player's score based on performance.
    """
    attempts = 0  # Keep track of the number of attempts
    score = 0  # Initialize the player's score

    print(f"\nI have chosen a number between {range_start} and {range_end}. Can you guess it?")
    if max_attempts:
        print(f"You have {max_attempts} attempts. Good luck!")

    while True:
        try:
            # Prompt the player to make a guess
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
            attempts += 1  # Increment the attempt count
            
            # Check if the guess is within the valid range
            if guess < range_start or guess > range_end:
                print(f"Please guess a number between {range_start} and {range_end}.")
            elif guess < secret_number:
                print("Too low! Try again.")  # Provide feedback for a low guess
            elif guess > secret_number:
                print("Too high! Try again.")  # Provide feedback for a high guess
            else:
                # The player guessed correctly
                print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                score += (max_attempts - attempts + 1) if max_attempts else 100 // attempts  # Calculate score
                print(f"Your score: {score}")
                break

            # End the game if the player has used all attempts
            if max_attempts and attempts >= max_attempts:
                print(f"Game Over! You've used all your {max_attempts} attempts. The number was {secret_number}.")
                break

        except ValueError:
            # Handle non-numeric input during guesses
            print("Invalid input! Please enter a valid number.")
    
    return score  # Return the player's score


def number_guessing_game():
    """
    Main function to coordinate the game. Handles setup, gameplay, and replay options.
    """
    while True:
        # Set up the game by calling the setup function
        difficulty, max_attempts, secret_number, range_start, range_end = game_setup()
        
        # Start the gameplay
        score = play_game(difficulty, max_attempts, secret_number, range_start, range_end)

        # Ask the player if they want to replay the game
        replay = input("Would you like to play again? (yes/no): ").strip().lower()
        if replay not in ['yes', 'y']:
            print("Thanks for playing! Goodbye.")
            break

# Run the game only if this script is executed directly
if __name__ == "__main__":
    number_guessing_game()