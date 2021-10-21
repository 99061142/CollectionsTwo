from random import randrange


def choose_dices():
    all_dices_chosen = False # If the user wants to go to the next throw

    attempt = 1 # The number of the attempt the user is on
    dices = [] # All the dices the user can choose from
    user_dices = [] # The dices the user has chosen


    # If the user did not choose 5 numbers, and have an amount of attempts left
    while attempt <= 3 and not all_dices_chosen:
        new_dice_amount = 5 - len(dices) # Amount of dices that mjust be added

        # Add numbers in the dice array
        for i in range(new_dice_amount):
            dice_num = randrange(1, 7) # Choose a random number between 1 and 6

            dice_str = str(dice_num) # Change the number to a string

            dices.append(dice_str) # Add the string inside the array

        # If the dices are added
        else:
            users_choose_dice = True # If the user must choose a number

            # If the user is choosing numbers to hold back, and the user has not stopped the question / not picked every number
            while users_choose_dice and len(dices) > 0 and len(user_dices) < 5:
                print('De dobbelstenen zijn:', dices)
                choose_dice = input('Wilt u enkele dobbelstenen opzij leggen? Als u getallen opzij wilt leggen moet je het getal zeggen, anders "nee":')

                if choose_dice != "nee":
                    try:    
                        dices.remove(choose_dice) # Remove the choice
                        user_dices += choose_dice # Add the choice inside the users dices array

                    except ValueError:
                        print('Kies een getal die u ook heeft gegooid, of typ "stop" om te stoppen')

                else:
                    users_choose_dice = False # The user go to the next throw

            # If the user don't want to choose more numbers
            else:
                if len(dices) > 0:            
                    attempt += 1 # Add 1 attempt

                else:
                    all_dices_chosen = True # If every number is chosen 

    # If the max throws are over, or the user did choose 6 numbers
    else:
        return user_dices # Return the numbers the user has chosen


user_dices = choose_dices() 

print(user_dices)