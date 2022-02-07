red_numbers = [-2, 0, 2, '', '', '', 7, 10, '', ''] # Red row
blue_numbers = ['', '', '', '', '', '', '', '', '', -2] # Blue row


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


def get_possible_positions(chosen_number:int, board_color:str) -> list:
    possible_positions = [False] * 10 # List with the possible positions
    
    array = red_numbers # Test array


    # Check every value inside the array
    for index, value in enumerate(array):
        previous_value = get_previous_value(index, chosen_number, array, board_color)
        next_value = get_next_value(index, chosen_number, array, board_color)


        # If the value is empty
        if isinstance(value, str):
            # If the previous value is empty
            if isinstance(previous_value, str): 
                possible_positions[index] = True # Possible position

                # If the next value is not empty
                if isinstance(next_value, int): 
                    """
                    if the next value is not correct
                    (higher than the chosen number for the red row
                    lower than the chosen number for the blue row)
                    """
                    if next_value >= chosen_number and board_color == "red" or next_value <= chosen_number and board_color == "blue":   
                        break
            
            # If the previous value is not empty
            else:
                """
                if the previous value is correct
                (lower than the chosen number for the red row
                higher than the chosen number for the blue row)
                """                
                if previous_value < chosen_number and board_color == "red" or previous_value > chosen_number and board_color == "blue":
                    possible_positions[index] = True


    return possible_positions


def main():
    number = 5 # Test number

    possible_positions = get_possible_positions(number, "red") # Get the possible positions inside the row
    print(possible_positions)




# When the progrma starts
if __name__ == "__main__":
    main()