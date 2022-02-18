from random import choice

color_cards_list = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
special_cards_dict = {"red": 2, "yellow": 2, "green": 2, "blue": 2}

cards = {
    "red": color_cards_list.copy(),
    "yellow": color_cards_list.copy(),
    "green": color_cards_list.copy(),
    "blue": color_cards_list.copy(),
    "draw-two": special_cards_dict.copy(),
    "reverse": special_cards_dict.copy(),
    "skip": special_cards_dict.copy(),
    "wild": 4,
    "draw-four": 4
}


# Get the amount of players
def ask_player_amount() -> int:
    player_amount_choosing = True # If the user must choose an amount
    
    # If the user must choose an amount
    while player_amount_choosing:
        chosen_player_amount = input("How many players do you want to play with? (2-10): ")

        # Check if the chosen value is a number
        if chosen_player_amount.isdigit():
            chosen_player_amount = int(chosen_player_amount)
            
            # If the user chose between 2 and 10
            if chosen_player_amount >= 2 and chosen_player_amount <= 10:
                player_amount_choosing = False
        else:  
            print("Choose an even number between 2 and 10")

    return chosen_player_amount


# Get random cards for every player
def card_amount_per_player(player_amount:int) -> dict:
    player_decks = {} # All the cards for the players
    
    for player_num in range(player_amount):
        player_name = player_num + 1 # Player name
        player_decks[player_name] = [] # Player cards

        # Get 7 random cards
        for _ in range(7):
            key = choice(list(cards)) # Card color / special name
    
            key_value = cards[key] # Get all the cards with the specific color or speciality

            # If the value inside the key is an number
            if isinstance(key_value, int):
                card_name = key # Card name thats get added to the player

                cards[key] -= 1 # Decrease the amount of cards by 1

                # If the amount of cards is 0
                if not cards[key]:
                    del cards[key] # Delete the specific key name for the card

            # If the value inside the key is an list
            elif isinstance(key_value, list):
                card_number = choice(key_value) # Random number of the color

                card_name = f"{key}_{card_number}" # Card name thats get added to the player

                cards[key].remove(card_number) # Remove the number

                # If the list with the numbers for the color are empty
                if not len(key_value):
                    del cards[key] # Delete the specific key name for the card
            
            # If the value inside the key is an dictionary
            else:
                color_key = choice(list(key_value)) # Get all the colors inside the head key

                card_name = f"{color_key}_{key}" # Card name thats get added to the player

                cards[key][color_key] -= 1 # Decrease the amount of cards by 1

                # If the dictionary with the numbers for the color are empty
                if not cards[key][color_key]:
                    del cards[key][color_key] # Delete the color key

                    # If all the colors are empty
                    if not cards[key]:
                        del cards[key] # Delete the specific key name for the card

            player_decks[player_name].append(card_name) # Add the random chosen card to the player

    return player_decks




# When the program starts
if __name__ == "__main__":
    player_amount = ask_player_amount() # Ask the amount of players
    player_decks = card_amount_per_player(player_amount) # Get the decks for the player