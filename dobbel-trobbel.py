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
        possible_positions[row_color] = [False] * len(board[row_color])

        array = board[row_color] # Numbers in the row

        for index, value in enumerate(array):
            if row_color == "white":
                if isinstance(value, str):
                    possible_positions[row_color][index] = True
            else:
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
def get_number_options(throwed_dices:dict, highest_lowest:dict) -> dict:
    number_options = {} # Numbers the user can choose

    # Value of the color dice
    red_dice = throwed_dices['red']
    blue_dice = throwed_dices['blue']
    white_dice = throwed_dices['white']

    # Add the options to the list
    number_options['a'] = blue_dice + red_dice + white_dice
    number_options['b'] = blue_dice + red_dice - white_dice
    number_options['c'] = blue_dice + red_dice
    number_options['d'] = highest_lowest['highest']['number'] - highest_lowest['lowest']['number']

    return number_options


# Let the user choose a number
def choose_number(number_options:dict) -> str:
    choosing_character = True # If the user must choose a number which is an option

    # While the user did not choose a number which is an option
    while choosing_character:
        for number_character, number_option in zip(number_options, number_options.values()):
            print(f"{number_character}: {number_option}", end="\n")

        chosen_character = input("Which number do you want to choose? Choose between the characters: ").lower()

        # If the user did choose a number which is an option
        if chosen_character in number_options:
            choosing_character = False

    return chosen_character

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


def show_possible_positions(possible_positions:dict):
    # For every row the user can choose from
    for color in possible_positions:
        row_values = [str(value) for value in board[color]] # All values as string

        print(f"{color}:", end=" ")

        # Show the values in the row, and the possible positions the user can choose from
        for value, possible_position in zip(row_values, possible_positions[color]):
            # If the position is not possible
            if not possible_position:
                print(f"| {value} |", end="   ")
            
            # If the position is possible
            else:
                print(f"| x |", end="   ")

        else:   
            print("\n", end="\n")


def choose_position(chosen_number:int, possible_positions:dict): 
    choosing_position = True # If the user must choose a possible position

    # If the user did not choose a possible position
    while choosing_position:
        chosen_position = input(f"Choose a possible position (x) for the number {chosen_number} (Examples: (color) 1, (color) 2, etc...): ")

        # Check if the user answered the question correectly
        try:
            chosen_position_information = chosen_position.split()
            
            chosen_color = chosen_position_information[0]
            chosen_position = int(chosen_position_information[1]) - 1

            board[chosen_color][chosen_position]
        
        # If the user did not answered the question correctly
        except (KeyError, IndexError, ValueError):
            pass
        
        # If the user answered the question correctly
        else:
            # Check if the chosen color is the row color the user can choose from
            if chosen_color in possible_positions.keys():
                # If the user chose a number that is not out of the row
                if chosen_position >= 0 and chosen_position < len(board[chosen_color]):   
                    # If the position is empty     
                    if possible_positions[chosen_color][chosen_position]:
                        board[chosen_color][chosen_position] = chosen_number # Add the chosen number to the row

                        choosing_position = False 


# Get the number from the character the user chose
def get_number_from_character(number_options:dict, chosen_character:str) -> int:
    return number_options[chosen_character]


def check_add_white_row(chosen_character:str) -> bool:
    add_white_dice = True if chosen_character == "c" or chosen_character == "d" else False

    return add_white_dice


def main():
    show_board() # Show the current board
    throwed_dices = throw_dices() # Throw the random dices
    highest_lowest = highest_lowest_numbers(throwed_dices) # Get the highest and lowest dice information
    number_options = get_number_options(throwed_dices, highest_lowest) # Get the possible numbers the user can choose
    chosen_character = choose_number(number_options) # Let the user choose a possible character for the number
    chosen_number = get_number_from_character(number_options, chosen_character)
    acceptable_rows = get_adding_color(highest_lowest) # Get the color(s) of the rows the user can add the number
    possible_positions = get_possible_positions(chosen_number, acceptable_rows) # Get the possible positions inside the row

    show_possible_positions(possible_positions) # Show the possible row(s), with the possible position(s) in it
    choose_position(chosen_number, possible_positions)# Let the user choose a possible position to place the number

    # If the must must add the white dice to the white row
    if check_add_white_row(chosen_character):
        white_dice = throwed_dices['white'] # White dice the user rolled

        possible_white_positions = get_possible_positions(white_dice, ['white']) # Get the possible positions in the white row
        show_possible_positions(possible_white_positions) # Show the white row, with the possible position(s) in it
        choose_position(white_dice, possible_white_positions) # Let the user choose a possible position to place the number




# When the progrma starts
if __name__ == "__main__":
    main()