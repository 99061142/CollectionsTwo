from random import choice


chosen_red_dices = [-2, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] # Stadard values for the red scoreboard
chosen_blue_dices = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-2'] # Stadard values for the blue scoreboard
chosen_white_dices = [' ', ' ', ' ', ' ', ' '] # Stadard values for the white scoreboard


# Scoreboard
def show_scoreboard():
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


def roll_dices():
    red_blue_dice = (1,2,3,4,5,6) # Blue Dice amounts
    white_dice = (1,1,1,2,2,3) # White Dice amounts

    rolled_red_dice = choice(red_blue_dice)
    rolled_blue_dice = choice(red_blue_dice)
    rolled_white_dice = choice(red_blue_dice)
    rolled_dices = [rolled_red_dice, rolled_blue_dice, rolled_white_dice] # All rolled dices

    print(
        f"U heeft voor rood het getal {rolled_red_dice} gerold",
        f"Voor blauw het getal {rolled_blue_dice}", 
        f"En voor wit het getal {rolled_white_dice}",
        "",
        "Door de gerolde getallen kunt u kiezen uit deze getallen:",
        f"A {rolled_red_dice + rolled_blue_dice + rolled_white_dice}",
        f"B {rolled_red_dice + rolled_blue_dice - rolled_white_dice}",
        f"C {rolled_red_dice + rolled_blue_dice}",
        f"D {max(rolled_dices) - min(rolled_dices)}",
        sep="\n", end="\n"
    )



# When the program starts
if __name__ == "__main__":
    roll_dices()
    #show_scoreboard()