from random import randrange


# Ask the amount of players
def player_amount():
    player_amount_choosing = True # If the player chose a valid option

    # Loop the question if the answer is not a valid option
    while player_amount_choosing:   
        # Ask the amount of players (minimum = 0)
        try:
            player_amount = input("\n Met hoeveel spelers wilt u spelen? (1 = alleen 2 of hoger = samen met een ander persoon/personen): ")
        
            player_amount = int(player_amount)
    
        except ValueError:
            print("\n Kies een nummer", end="\n")

        else:
            if player_amount > 0:
                player_amount_choosing = False # Stop the quesiton
            
            else:
                print("\n Kies een nummer groter dan 0", end="\n")

    # If the user did choose a valid option
    else:
        return player_amount # Return the amount of players


# Ask the player names
def players_information(player_amount):
    players = {} # Array for the player names

    # Information
    print(
        "",
        "------------------------------------------------------------------------",
        "* Het getal geeft aan wanneer de speler begint (1 = begint als eerste) *",
        sep="\n", end="\n"
    )

    # Loop the question if the answer is not a valid option
    for num in range(player_amount):
        player_num = num + 1

        player_name_choosing = True # If the player chose a valid option

        # Loop the question if the answer is not a valid option
        while player_name_choosing:
            player = input(f"Hoe wilt u speler {player_num} noemen?: ")    

            # Check if the name is already in use
            if player in players:   
                print(f"De naam {player} is al in gebruik, kies een andere naam voor speler {player_num}", end="\n")
            
            else:
                players[player] = {} # Add the player to the dictionary
                player_name_choosing = False # Stop the question for the specific player

    # If all the names are chosen
    else:
        add_starting_information(players) # Add the arrays for all the players
        return players # Return the dictionary with the names


# Add more information to the players array
def add_starting_information(players):
    # Dictionary for all the combinations the user can make
    combinations = {
        "aces": {"valid": False, "points": 0},
        "twos": {"valid": False, "points": 0},
        "threes": {"valid": False, "points": 0},
        "fours": {"valid": False, "points": 0},
        "fives": {"valid": False, "points": 0},
        "sixes": {"valid": False, "points": 0},
        "three of a kind": {"valid": False, "points": 0},
        "four of a kind": {"valid": False, "points": 0},
        "full hourse": {"valid": False, "points": 25},
        "small straight": {"valid": False, "points": 30},
        "large straight": {"valid": False, "points": 40},
        "yahtzee": {"valid": False, "points": 50},
        "top score": {"valid": False, "points": 0},
        "chance": {"valid": False, "points": 0}
    }


    # Loop through every player
    for player in players:
        players[player]['dices'] = [] # Dices list for the random dices
        players[player]['dices_chosen'] = [] # Dices list for the dices the user chose
        players[player]['combinations'] = combinations # Combinations dictionary that the user can make


# Roll random dices
def roll_dices(players, player):
    user_dices = players[player]['dices_chosen'] # Dices the user did choose

    dice_amount = 5 - len(user_dices) # Amount of dices that must be added


    # Add random numbers into the dice array
    for _ in range(dice_amount):
        # Choose a random number between 1 and 6
        dice = randrange(1, 7)
        dice = str(dice)

        players[player]['dices'].append(dice) # Add the number to the array


# Let the user choose the dice(s) he want to put aside
def choose_dices(players, player):
    print(
        "",
        "---------------------------------",
        f"* spelers '{player}' beurt *",
        "---------------------------------",
        sep="\n", end="\n"
    )

    dice_choosing = True

    user_dices = players[player]['dices'] # The dices the user can choose from
    user_dices_chosen = players[player]['dices_chosen'] # The dices the user has chosen


    turn = 1

    show_turn(turn) # Show the amount of turns the user has left

    while dice_choosing and len(user_dices_chosen) < 5 and turn <= 3:
        # The dices the user can choose from
        dices_str = ", ".join(user_dices)
        
        if len(user_dices_chosen) > 0:
            user_dices_chosen_str = ", ".join(user_dices_chosen) # All the dices the user has chosen

            user_dices_information = f"De dobbelstenen die u apart heeft gelegd zijn: {user_dices_chosen_str}"
        else:
            user_dices_information = "U heeft nog geen stenen apart gelegd"

        print(
            "",
            f"{user_dices_information}",
            f"Uw dobbelstenen waaruit u kan kiezen zijn: {dices_str} (al {str( len(user_dices_chosen) )} stenen apart gelegd).",
            sep="\n", end="\n"
        )

        
        dice = input("Als u een steen apart wilt leggen typ het getal, als je de stenen nog een keer wil rollen typ 'overnieuw': ")

        if dice in user_dices:
            players[player]['dices'].remove(dice) # Remove the dice the user has chosen

            players[player]['dices_chosen'].append(dice) # Add the dice to the users dices

        else:
            print("Kies een getal die geworpen is of typ 'overnieuw'")


        if dice == "overnieuw":
            turn += 1

            if turn <= 3:
                show_turn(turn) # Show the amount of turns the user has left


# Show the amount of turns the user has left
def show_turn(turn):
    print(
        "",
        "----------------------------------------------------------------------------------------------",
        f"U heeft nog {4 - turn} beurten over, daarna worden de overige stenen bij uw stenen toegevoegd",
        "----------------------------------------------------------------------------------------------",
        sep="\n", end="\n"
    )


# Switch to the next player
def switch_player(player_names, players, player):
    players[player]['dices'] = [] # Reset the random dices
    players[player]['dices_chosen'] = [] # Reset the dices the user did choose

    new_player_index = player_names.index(player) + 1 # Get the next player index

    try:
        player = player_names[new_player_index] # Get the next player
    except IndexError:
        player = player_names[0] # Get the first player
    finally:
        return player # Return the players name


# Game functions
def game(players):
    player_names = list(players.keys()) # Make a list of all the player names

    player = player_names[0] # Starting player


    game_being_played = True # If the game is not over

    # If all the players are not done with the game
    while game_being_played:    
        roll_dices(players, player) # Roll the random dices
        choose_dices(players, player) # The user can choose a dice
        player = switch_player(player_names, players, player) # Switch to the next player


# Get the starting information, and start the game
def main():
    amount = player_amount() # Get the amount of players
    players = players_information(amount) # Ask every name of the player
    game(players) # Start the game




# If the code starts
if __name__ == "__main__":
    main()