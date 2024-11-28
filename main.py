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

print(game_setup())