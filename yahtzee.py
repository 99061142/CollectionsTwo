from random import randrange
from time import sleep


dices = []
user_dices = []


# Ask the total amount of players
def choose_player_amount():
    solo_or_with_choosing = True # Loop through the solo or with more players question

    # If the user must choose 'alleen' or 'meerdere' 
    while solo_or_with_choosing:   
        solo_or_with = input("Wilt u alleen of met meerdere mensen spelen?: ").lower()

        if solo_or_with == "alleen":
            player_amount = 1
            solo_or_with_choosing = False # Go out of the question

        elif solo_or_with == "meerdere":
            player_amount_choosing = True # Loop through the total amount of players question

            # If the user did not choose a valid number of players
            while player_amount_choosing:
                player_amount = input("Met hoeveel spelers wilt u spelen?: ")

                try:
                    player_amount = int(player_amount) # Check if its a valid number
                except ValueError:
                    print("Kies een geldig aantal (1, 2, 3, etc...)") # Return the error message

                # If its a valid number
                else:
                    player_amount_choosing = False # Go out of the question how many players are gonna play this game
                    solo_or_with_choosing = False # Go out of the question if the user wants to play solo or with more players
        
        else:
            print("Kies tussen 'alleen' of 'meerdere'")
    
    else:
        return player_amount # Return the total amount of players


def get_players_names(player_amount):
    players = [] # Array for the player names

    print("\n * Het getal geeft aan wanneer de speler begint (1 = begint als eerste) * \n")

    # Loop through the amount of players to ask the names
    for num in range(player_amount):
        player_num = num + 1

        player = input(f"Hoe wilt u speler {player_num} noemen?: ")    

        players.append(player) # Add the name to the player names array

    else:
        return players # Return the array with names


def roll_dices():
    global dices
    global user_dices

    dice_amount = 5 - len(user_dices) # Amount of dices that must be added

    # Add random numbers in the dice array
    for _ in range(dice_amount):
        random_num = randrange(1, 7) # Choose a random number between 1 and 6

        dice = str(random_num) 

        dices.append(dice) # Add the random number to the array
    
    else:
        return dices # Return the dices the user can choose from


def choose_dices(player):
    global dices
    global user_dices

    print(f"\n * spelers '{player}' beurt *")


    dice_choosing = True

    while dice_choosing and len(user_dices) < 5:
        dices_str = ", ".join(dices) # All the dices
        
        if len(user_dices) > 0:
            user_dices_str = ", ".join(user_dices) # All the dices the user has chosen

            print(f"\n De dobbelstenen die u apart heeft gelegd zijn: {user_dices_str} \n")
        
        else:
            print("\n U heeft nog geen dobbelstenen apart gelegd \n")
        
        dice = input(f"Uw dobbelstenen waaruit u kan kiezen zijn: {dices_str} (al {len(user_dices)} stenen apart gelegd), als u een steen apart wilt leggen typ het getal, anders typ 'stop': ")

        if dice in dices:
            dices.remove(dice) # Remove the dice the user has chosen

            user_dices.append(dice) # Add the dice to the users dices

        elif dice == "stop":
            dice_choosing = False # Go out of the question to choose a dice

        else:
            print("Kies een getal die geworpen is of typ 'stop'")

    else:
        dices = [] # Remove all the dices

        return user_dices # Return the dices the user has chosen


def switch_player(players, player):
    global dices
    global user_dices

    dices = []
    user_dices = []

    try:
        old_index = players.index(player) # Get the index of the old player 
        new_index = old_index + 1 # Get the new index
        
        player = players[new_index] # Get the next player
    except IndexError:
        player = players[0] # Get the first player
    finally:
        return player # Return the new player


def game_starting(player_amount, players):
    global dices
    global user_dices


    player = players[0] # Get the first player

    game_being_played = True

    while game_being_played:
        throwing_amount = 1
        max_throwing_amount = 3

        # If the game is being played
        while throwing_amount <= max_throwing_amount:
            dices = roll_dices() # Get all the dices the user can choose from

            user_dices = choose_dices(player) # Ask the user which dice he wants


            throwing_amount += 1

        else:
            throwing_amount = 1
            max_throwing_amount = 3

            player = switch_player(players, player)


def main():
    player_amount = choose_player_amount() # Get the total amount of players

    players = get_players_names(player_amount) # Get an array with all the player names

    game_starting(player_amount, players)




if __name__ == "__main__": 
    main()