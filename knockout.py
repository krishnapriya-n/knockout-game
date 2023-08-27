from random import randint
from time import sleep

# Introduction and game rules
print("KNOCKOUT")
print("This is a dice game where each player chooses a 'knockout number' - which is either a 6, 7, 8, or 9")
print("Players take turns throwing both dice, once each turn")
print("If the two rolled dice numbers add up to be the chosen number, the player will be eliminated")
print("The game will now begin")
print("--------------------")

# Function to get a valid number from the player
def get_player_number(player):
    while True:
        try:
            number = int(input(f"{player}: Please enter a number from 6, 7, 8, or 9: "))
            if 6 <= number <= 9:
                return number
            else:
                print(f"{player}: Please enter a valid number")
        except ValueError:
            print(f"{player}: Please enter a valid number")

# Function to simulate rolling a die
def roll_die(player):
    print(f"Rolling the die for {player}")
    sleep(3)
    return randint(1, 6)

# Main game loop
while True:
    # Get knockout numbers from players
    player1_number = get_player_number("Player 1")
    player2_number = get_player_number("Player 2")

    # Roll the dice for each player
    player1_die_1 = roll_die("Player 1")
    player2_die_1 = roll_die("Player 2")
    player1_die_2 = roll_die("Player 1")
    player2_die_2 = roll_die("Player 2")

    print(f"Player 1 dice: {player1_die_1}, {player1_die_2}")
    print(f"Player 2 dice: {player2_die_1}, {player2_die_2}")

    # Check if the players are knocked out or have survived
    if player1_die_1 + player1_die_2 == player1_number:
        print("Player 1: You have been knocked out")
    else:
        print("Player 1 has survived")

    if player2_die_1 + player2_die_2 == player2_number:
        print("Player 2: You have been knocked out")
    else:
        print("Player 2 has survived")

    # Ask if players want to replay
    replay = input("Would you like to replay (enter yes / no): ")
    if replay.lower() != "yes":
        break
