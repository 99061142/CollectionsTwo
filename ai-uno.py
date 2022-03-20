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

card_points = {
    "draw_two": 20,
    "reverse": 20,
    "skip": 20,
    "wild": 50,
    "draw_four": 50
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
def create_player_decks(player_amount:int) -> dict:
    player_decks = {player_number: [] for player_number in list(range(1,player_amount+1))} # List of player cards

    # Pick 7 cards for every player
    for i in range(7):
        for player in range(1, player_amount+1):
            card_type = choice(list(cards.keys())) # Random card type
            card_options = cards[card_type] # Options for the card type

            # If the option is a number (card type)
            if(isinstance(card_options, int)): 
                cards[card_type] -= 1 # Pick 1 card out of the deck

                card_name = card_type # Save the card name, to add it inside the deck of player cards 

            # If the option is a list (card type + number)
            elif isinstance(card_options, list):
                card_number = choice(card_options)

                cards[card_type].remove(card_number) # Pick 1 card out of the deck

                card_name = f'{card_type}_{card_number}' # Save the card name, to add it inside the deck of player cards 

            # If the option is a dict (card type + color + number)
            elif isinstance(card_options, dict):
                card_color = choice(list(card_options.keys()))

                cards[card_type][card_color] -= 1 # Pick 1 card out of the deck

                card_name = f'{card_type}_{card_color}' # Save the card name, to add it inside the deck of player cards 

                # If every card is used for the color of the card type
                if(not cards[card_type][card_color]):
                    del cards[card_type][card_color] # Delete the color for the card type


            # If every card is used for the card type
            if(not cards[card_type]):
                del cards[card_type] # Delete the card type

            player_decks[player].append(card_name) # Add the card name to the deck of the specific user

    return player_decks



# When the program starts
if __name__ == "__main__":
    player_amount = ask_player_amount() # Ask the amount of players
    player_decks = create_player_decks(player_amount) # Get the decks for the player