from random import choice

board = {
    "red": [-2, '', '', ' ', ' ', ' ', '', '', ' ', ' '],
    "blue": [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', -2],
    "white": [' ', ' ', ' ', ' ', ' ']
}

dices = {
    "red": (1, 2, 3, 4, 5, 6),
    "blue": (1, 2, 3, 4, 5, 6),
    "white": (1, 1, 1, 2, 2, 3)
}


# Get the previous value in the row
def get_previous_value(index:int, chosen_number:int, array:list, board_color:str):
    # If the index position is not the start
    if index - 1 >= 0:
        previous_value = array[index-1] # Get the previous value
    else:
        previous_value = chosen_number - 1 if board_color == "red" else chosen_number + 1 # Get a number that always be correct for the game

    return previous_value


# Get the next value in the row
def get_next_value(index:int, chosen_number:int, array:list, board_color:str):
    # If the index position is not the end
    if index < len(array) - 1:
        next_value = array[index+1] # Get the next value
    else:
        next_value = chosen_number + 1 if board_color == "red" else chosen_number - 1 # Get a number that always be correct for the game

    return next_value


# Check which position is free in the board
def get_possible_positions(chosen_number:int, acceptable_rows:list) -> dict:
    possible_positions = {} # List with the possible positions
    
    # For every possible row
    for row_color in acceptable_rows:
        possible_positions[row_color] = [False] * 10

        array = board[row_color] # Numbers in the row

        for index, value in enumerate(array):
            previous_value = get_previous_value(index, chosen_number, array, row_color)
            next_value = get_next_value(index, chosen_number, array, row_color)


            # If the value is empty
            if isinstance(value, str):
                # If the previous value is empty
                if isinstance(previous_value, str): 
                    possible_positions[row_color][index] = True # Possible position

                    # If the next value is not empty
                    if isinstance(next_value, int): 
                        """
                        if the next value is not correct
                        (higher than the chosen number for the red row
                        lower than the chosen number for the blue row)
                        """
                        if next_value >= chosen_number and row_color == "red" or next_value <= chosen_number and row_color == "blue":   
                            break
                
                # If the previous value is not empty
                else:
                    """
                    if the previous value is correct
                    (lower than the chosen number for the red row
                    higher than the chosen number for the blue row)
                    """                
                    if previous_value < chosen_number and row_color == "red" or previous_value > chosen_number and row_color == "blue":
                        possible_positions[row_color][index] = True

    return possible_positions


# Show the board
def show_board():
    # For every row color
    for color in board:
        row_values = [str(value) for value in board[color]] # All values as string

        print(f"{color}: ", end="")

        # For every value
        for value in row_values:
            print(f"| {value} |", end="   ")
        else:   
            print("\n", end="\n")


# Throw the dices
def throw_dices() -> dict:
    throwed_dices = {}

    # Throw every dice
    for color in dices:
        throwed_dices[color] = choice(dices[color]) # Add the random chosen number

    #throwed_dices = {"red": 5, "blue": 5, "white": 1} # Test dictionary

    return throwed_dices


# Get the number that is the lowest and highest
def highest_lowest_numbers(throwed_dices:dict) -> dict:
    highest_lowest = {"highest": {}, "lowest": {}, "equal": False}

    dice_values = throwed_dices.copy() # Copy the throwed dices information
    del dice_values['white'] # Delete the white dice information


    dice_values_list = list(dice_values.values()) # All the dice values

    # If every value is the same
    if dice_values_list.count(dice_values_list[0]) == len(dice_values_list):
        highest_lowest['equal'] = True


    highest_lowest['highest']['color'] = max(dice_values, key=dice_values.get) # Highest dice color
    highest_lowest['lowest']['color'] = min(dice_values, key=dice_values.get) # Lowest dice color
    highest_lowest['highest']['number'] = max(dice_values.values()) # Highest dice value
    highest_lowest['lowest']['number'] = min(dice_values.values()) # Lowest dice value

    return highest_lowest


# Calculate the possible numbers
def get_number_options(throwed_dices:dict, highest_lowest:dict) -> list:
    number_options = [] # List where the options gets stored

    # Value of the color dice
    red_dice = throwed_dices['red']
    blue_dice = throwed_dices['blue']
    white_dice = throwed_dices['white']

    # Add the options to the list
    number_options.extend([
        blue_dice + red_dice + white_dice,
        blue_dice + red_dice - white_dice,
        blue_dice + red_dice,
        highest_lowest['highest']['number'] - highest_lowest['lowest']['number']
    ])

    return number_options


# Let the user choose a number
def choose_number(number_options:list) -> int:
    number_options = [str(value) for value in number_options] # All values as string

    choosing_number = True # If the user must choose a number which is an option

    # While the user did not choose a number which is an option
    while choosing_number:
        chosen_number = input(f"Which number do you want to choose? Choose between {', '.join(number_options)}: ")

        # If the user did choose a number which is an option
        if chosen_number in number_options:
            choosing_number = False

    return int(chosen_number)


# Get the row color on which the user can add the chosen number
def get_adding_color(highest_lowest:dict) -> list:
    acceptable_rows = []

    # If the lowest and highest value are the same
    if highest_lowest['equal']:
        acceptable_rows.extend(["red", "blue"]) # Add both colors
    else:
        # Add the lowest color
        lowest_throwed_color = highest_lowest['highest']['color']
        acceptable_rows.append(lowest_throwed_color)

    return acceptable_rows


def main():
#    show_board()


    throwed_dices = throw_dices()
    highest_lowest = highest_lowest_numbers(throwed_dices)
    number_options = get_number_options(throwed_dices, highest_lowest)
    chosen_number = choose_number(number_options)
    acceptable_rows = get_adding_color(highest_lowest)
    possible_positions = get_possible_positions(chosen_number, acceptable_rows) # Get the possible positions inside the row


    print(possible_positions)



# When the progrma starts
if __name__ == "__main__":
    main()