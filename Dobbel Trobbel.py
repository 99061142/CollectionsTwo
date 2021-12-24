from random import choice


chosen_red_dices = [-2, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] # Stadard values for the red scoreboard
chosen_blue_dices = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-2'] # Stadard values for the blue scoreboard
chosen_white_dices = [' ', ' ', ' ', ' ', ' '] # Stadard values for the white scoreboard


# Scoreboard
def show_scoreboard():
    chosen_red_dices_str = [f"| {dice} |" for dice in chosen_red_dices] # Make a list of the red values
    chosen_blue_dices_str = [f"| {dice} |" for dice in chosen_blue_dices] # Make a list of the blue values
    chosen_white_dices_str = [f"| {dice} |" for dice in chosen_white_dices] # Make a list of the white values

    # Add spaces between the chosen dices
    chosen_red_dices_str = '   '.join(chosen_red_dices_str)
    chosen_blue_dices_str = '   '.join(chosen_blue_dices_str)
    chosen_white_dices_str = '   '.join(chosen_white_dices_str)


    print(
        "",
        "-" * len(chosen_red_dices_str),
        f"{chosen_red_dices_str}",
        "-" * len(chosen_red_dices_str),
        "",
        "-" * len(chosen_blue_dices_str),
        f"{chosen_blue_dices_str}",
        "-" * len(chosen_blue_dices_str),
        "",
        "-" * len(chosen_white_dices_str),
        f"{chosen_white_dices_str}",
        "-" * len(chosen_white_dices_str),
        sep="\n", end="\n"
    )


# Let the user choose a letter to add the number to the scoreboard
def choose_letter(allowed_options):

    letter_choosing = True

    while letter_choosing:
        chosen_letter = input("Kies de letter voor het getal: ").upper()

        if chosen_letter in list(allowed_options):
            letter_choosing = False

        else:
            allowed_letters = [f"'{letter}'" for letter in allowed_options]
            print(f"kies {', '.join(allowed_letters)}")

    else:
        return allowed_options[chosen_letter] # Return the chosen number


def roll_dices():
    red_blue_dice = (1,2,3,4,5,6) # Blue Dice amounts
    white_dice = (1,1,1,2,2,3) # White Dice amounts

    rolled_red_dice = choice(red_blue_dice)
    rolled_blue_dice = choice(red_blue_dice)
    rolled_white_dice = choice(red_blue_dice)
    rolled_dices = [rolled_red_dice, rolled_blue_dice, rolled_white_dice] # All rolled dices

    allowed_options = {
        "A": rolled_red_dice + rolled_blue_dice + rolled_white_dice,
        "B": rolled_red_dice + rolled_blue_dice - rolled_white_dice,
        "C": rolled_red_dice + rolled_blue_dice,
        "D": max(rolled_dices) - min(rolled_dices)
    }

    print(
        f"U heeft voor rood het getal {rolled_red_dice} gerold",
        f"Voor blauw het getal {rolled_blue_dice}", 
        f"En voor wit het getal {rolled_white_dice}",
        "",
        "Door de gerolde getallen kunt u kiezen uit deze getallen:",
        sep="\n", end="\n"
    )
    
    # Show the numbers the user can choose from
    for key, value in allowed_options.items():
        print(f"{key} {value}", end="\n")
    else:
        print("", end="\n")

    return allowed_options



def main():
    allowed_options = roll_dices()
    chosen_number = choose_letter(allowed_options)

    show_scoreboard()


# When the program starts
if __name__ == "__main__":
    main()