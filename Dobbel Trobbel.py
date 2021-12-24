red_dice = (1,2,3,4,5,6) # Blue Dice amounts
blue_dice = (1,1,1,2,2,3) # White Dice amounts


chosen_red_dices = [-2, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] # Stadard values for the red scoreboard
chosen_blue_dices = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-2'] # Stadard values for the blue scoreboard
chosen_white_dices = [' ', ' ', ' ', ' ', ' '] # Stadard values for the white scoreboard


# Scoreboard
def scoreboard():
    chosen_red_dices_str = [f"| {dice} |" for dice in chosen_red_dices] # Make a list of the red values
    chosen_blue_dices_str = [f"| {dice} |" for dice in chosen_blue_dices] # Make a list of the blue values
    chosen_white_dices_str = [f"| {dice} |" for dice in chosen_white_dices] # Make a list of the white values


    print(
        "---------------------------------------------------------------------",
        f"{'  '.join(chosen_red_dices_str)}",
        "---------------------------------------------------------------------",
        "\n",
        "---------------------------------------------------------------------",
        f"{'  '.join(chosen_blue_dices_str)}",
        "---------------------------------------------------------------------",
        "\n",
        "                  ---------------------------------",
        f"                  {'  '.join(chosen_white_dices_str)}",
        "                  ---------------------------------",
        sep="\n", end="\n"
    )




# When the program starts
if __name__ == "__main__":
    scoreboard()