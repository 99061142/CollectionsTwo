from random import choice


chosen_red_dices = [-2, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] # Stadard values for the red scoreboard
chosen_blue_dices = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', -2] # Stadard values for the blue scoreboard
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

    # Show the scoreboard
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
        " " * (len(chosen_white_dices_str ) // 2) + "-" * len(chosen_white_dices_str),
        " " * (len(chosen_white_dices_str ) // 2) + f"{chosen_white_dices_str}",
        " " * (len(chosen_white_dices_str ) // 2) +"-" * len(chosen_white_dices_str),
        "",
        sep="\n", end="\n"
    )


# Count every number to get the total amount
def count_numbers(array):
    total_amount = 0 # Starting value

    # Loop through every value
    for value in array: 
        # If value gets added if it is a number
        if isinstance(value, int):
            total_amount += value
    else:
        return total_amount # Return the total amount


# Get the array with all the positions the user can choose from
def get_available_space(array, chosen_number):
    array_length = len(array) # Length of the array

    check_array = [True] * array_length # Starting list to check which position is free
    change_from_index = None # Upwards of this number every position is not free anymore (if its not None)

    # Loop through every value of the array
    for index, value in enumerate(array):
        # If the value is a number
        if isinstance(value, int):
            # If the value is higher than the number the user chose
            if value >= chosen_number:
                change_from_index = index # Set the value to change every value upwards of the index 
                break
            
            check_array[index] = False # Set the index to False to show that the position is taken

    # If the chosen number was lower than one of the values in the list
    if change_from_index != None:
        # Change every value upwards of the 'change_from_index' number
        for index in range(change_from_index - array_length, +1): 
            # Stop the loop when the starting value is reached
            if index == 0:  
                break
            else:
                check_array[index] = False # Set the free position to False

    return check_array # Return the list of positions the user can choose


# Show which positions the user can choose
def show_available_positions(chosen_number, array):
    # Loop through the dictionary with positions the user can take
    for key in array:
        for index, value in enumerate(array[key]):
            # If the position is free
            if value:
                print(f"rij met de kleur {key} plek {index}", end="\n") # Show the positon to the user
        else:  
            print("", end="\n")


# Add the chosen number to the scoreboard
def add_to_scoreboard(chosen_number):
    red_total = count_numbers(chosen_red_dices) # Get the total amount of the red dices on the scoreboard
    blue_total = count_numbers(chosen_blue_dices) # Get the total amount of the blue dices on the scoreboard

    available_space_dict = {} # Starting dictionary

    # If the red scoreboard has a lower total amount, or both have the same amount
    if red_total < blue_total or red_total == blue_total:
        available_space_dict['rood'] = get_available_space(chosen_red_dices, chosen_number)
    
    # If the blue scoreboard has a lower total amount, or both have the same amount
    if red_total > blue_total and red_total < blue_total or red_total == blue_total:
        available_space_dict['blauw'] = get_available_space(chosen_blue_dices, chosen_number)


    show_available_positions(chosen_number, available_space_dict) # Show which positions the user can take


# Let the user choose a letter to add the number to the scoreboard
def choose_letter(allowed_options):

    letter_choosing = True # If the user must choose a letter

    # If the user did not choose a valid option
    while letter_choosing:
        chosen_letter = input("Kies de letter voor het getal: ").upper()

        # If the letter is a valid option
        if chosen_letter in list(allowed_options):
            letter_choosing = False

        else:
            # Show the user which letters are valid
            allowed_letters = [f"'{letter}'" for letter in allowed_options]
            print(f"kies {', '.join(allowed_letters)}")

    else:
        return allowed_options[chosen_letter] # Return the chosen number


# Roll the random numbers for the dices
def roll_dices():
    red_blue_dice = (1,2,3,4,5,6) # Red / blue dice amounts
    white_dice = (1,1,1,2,2,3) # White Dice amounts

    # Choose a random number for the dices
    rolled_red_dice = choice(red_blue_dice)
    rolled_blue_dice = choice(red_blue_dice)
    rolled_white_dice = choice(white_dice)

    # Dictionary with all the options
    rolled_dices = [rolled_red_dice, rolled_blue_dice, rolled_white_dice] # All rolled dices

    allowed_options = {
        "A": rolled_red_dice + rolled_blue_dice + rolled_white_dice,
        "B": rolled_red_dice + rolled_blue_dice - rolled_white_dice,
        "C": rolled_red_dice + rolled_blue_dice,
        "D": max(rolled_dices) - min(rolled_dices)
    }

    # Show which numbers the user has rolled
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


    return allowed_options # Return the allowed options


def main():
    allowed_options = roll_dices() # Roll the dices for the user
    chosen_number = choose_letter(allowed_options) # Let the user choose a number to play with

    show_scoreboard() # Show the scoreboard

    add_to_scoreboard(chosen_number)




# When the program starts
if __name__ == "__main__":
    main()