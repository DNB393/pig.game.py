# This is a game of Pig

import random


def roll():
    """Simulates rolling a six-sided die."""
    return random.randint(1, 6)


# Get number of players
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid input, try again.")

# Game variables
max_score = 100
player_scores = [0] * players

# Game loop
while max(player_scores) < max_score:
    for player_idx in range(players):
        print(f"\nPlayer {player_idx + 1}, your turn has started!")
        print(f"Your total score is: {player_scores[player_idx]}\n")

        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y/n)? ").strip().lower()
            if should_roll != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn over.")
                break
            else:
                current_score += value
                print(f"You rolled a: {value}")
                print(f"Your score this turn is: {current_score}")

        # Add turn score to player's total score
        player_scores[player_idx] += current_score
        print(f"Your new total score is: {player_scores[player_idx]}")

        # Check if the player has won
        if player_scores[player_idx] >= max_score:
            print(f"\nPlayer {player_idx + 1} wins with a score of {player_scores[player_idx]}!")
            exit()  # Exit the game when a player wins

