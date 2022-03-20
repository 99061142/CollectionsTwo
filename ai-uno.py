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
    pass




# When the program starts
if __name__ == "__main__":
    player_amount = ask_player_amount() # Ask the amount of players
    player_decks = create_player_decks(player_amount) # Get the decks for the player