def ask_player_amount():
    player_amount_choosing = True # If the user must choose an amount
    
    # If the user must choose an amount
    while player_amount_choosing:
        chosen_player_amount = input("How many players do you want to play with? (2-10): ")

        # Check if the chosen value is a number
        try:
            chosen_player_amount = int(chosen_player_amount)
        
        # If the chosen value is not a number
        except ValueError:
            pass
        
        # If the chosen value is a number
        else:
            # If the user chose between 2 and 10
            if chosen_player_amount >= 2 and chosen_player_amount <= 10:
                player_amount_choosing = False

    return chosen_player_amount




# When the program starts
if __name__ == "__main__":
    player_amount = ask_player_amount() # Ask the amount of players