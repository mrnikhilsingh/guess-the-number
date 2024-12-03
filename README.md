# Guess The Number

A Python-based interactive game where players guess a randomly generated number. The game includes three difficulty levels, tracks the player's score, and provides an option to replay.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [How to run the game](#how-to-run-the-game)
5. [Code Overview](#code-overview)
   - Functions
6. [Game Flow](#game-flow)
7. [Contributors](#contributors)

## Introduction

The Guess The Number game is a fun way to practice programming concepts while creating an interactive user experience. Players choose a difficulty level, guess a number, and receive feedback until they guess correctly or exhaust their attempts.

## Features

- Three difficulty levels:
  - Easy: Unlimited attempts
  - Medium: 10 attempts
  - Hard: 5 attempts
- Randomly generated secret number between 1 and 100.
- Scoring system based on performance.
- Replay option to play multiple rounds.
- Input validation to handle errors gracefully.

## Requirements

- **Python:** Version 3.6 or higher.
- **Modules:** No external modules are required, the game uses Python's built-in `random` module.

## How to run the game

1. Ensure Python is installed on your system. To check, run:

```bash
python --version
```

2. Save the game code into a Python file, e.g., `guess_the_number.py`.

3. Open a terminal or command prompt, navigate to the file's directory, and run:

```bash
python guess_the_number.py
```

## Code Overview

The game code is modular, with each part handled by a separate function. Below is a breakdown of the main functions:

**1. game_setup()**

- Purpose: Initializes the game, allowing the player to choose a difficulty level and generating the secret number.
- Parameters: None
- Returns:
  - `difficulty`: Chosen difficulty level.
  - `max_attempts`: Maximum allowed attempts.
  - `secret_number`: Randomly generated number.
  - `range_start`, `range_end`: Range for the number.

**2. play_game()**

- Purpose: Manages the gameplay, including guessing logic, feedback, and score calculation.
- Parameters:
  - `difficulty`: The selected difficulty level.
  - `max_attempts`: Maximum allowed attempts.
  - `secret_number`: Randomly generated secret number.
  - `range_start`, `range_end`: Range of numbers for guessing.
- Returns:
  - `score`: Player's score based on performance.

**3. guess_the_number()**

- Purpose: Coordinates the overall game flow, integrates setup and gameplay, and handles the replay option.
- Parameters: None
- Returns: None

## Game Flow

**1. Setup Phase:**

- The player chooses a difficulty level.
- The game generates a secret number.

**2. Gameplay Phase:**

- The player makes guesses within the defined range.
- The game provides feedback (Too low, Too high, or Correct).
- Score is calculated based on attempts.

**3. Replay Phase:**

- The player is prompted to play again or exit.

## Sample Output

**Example 1: Correct guess**

```mathematica
Welcome to the Guess The Number Game!
Choose a difficulty level:
1. Easy (Unlimited attempts)
2. Medium (10 attempts)
3. Hard (5 attempts)
Enter your choice (1/2/3): 2

I have chosen a number between 1 and 100. Can you guess it?
You have 10 attempts. Good luck!
Attempt 1: Enter your guess: 50
Too low! Try again.
Attempt 2: Enter your guess: 75
Too high! Try again.
Attempt 3: Enter your guess: 62
🎉 Congratulations! You guessed the number 62 in 3 attempts.
Your score: 8
Would you like to play again? (yes/no): no
Thanks for playing! Goodbye.
```

**Example 2: Game Over**

```mathematica
Welcome to the Enhanced Number Guessing Game!
Choose a difficulty level:
1. Easy (Unlimited attempts)
2. Medium (10 attempts)
3. Hard (5 attempts)
Enter your choice (1/2/3): 3

I have chosen a number between 1 and 100. Can you guess it?
You have 5 attempts. Good luck!
Attempt 1: Enter your guess: 30
Too low! Try again.
Attempt 2: Enter your guess: 80
Too high! Try again.
Attempt 3: Enter your guess: 60
Too low! Try again.
Attempt 4: Enter your guess: 70
Too high! Try again.
Attempt 5: Enter your guess: 65
Game Over! You've used all your 5 attempts. The number was 67.
Would you like to play again? (yes/no): no
Thanks for playing! Goodbye.
```

## Contributors

- **[Nikhil Singh](https://github.com/mrnikhilsingh):**
  - Designed the `game_setup()` function to manage game initialization and difficulty selection and prepared comprehensive project documentation.
- **[Poorvi Jain](https://github.com/poorvi-dev):**
  - Developed the `play_game()` function for gameplay logic, including guesses and scoring.
- **[Mahak](https://github.com/Mahak96):**
  - Created the `guess_the_number()` function to integrate all components and manage replay functionality.

## Future Enhancements

- Add a timer to track the time taken to guess the number.
- Include hints for players (e.g., divisible by a certain number).
- Expand difficulty levels with larger ranges or varying rules.
