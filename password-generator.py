import string 
import random

def generate_random_password(total_len):
    password_position = False # If the password is not valid

    password = [] # Array for the password

    uppercase_amount = random.randrange(2, 6) # Uppercase characters amount
    random_num_amount = random.randrange(4, 7) # Number characters amount

    lowercase_amount = total_len - (uppercase_amount + random_num_amount + 3) # Lowercase characters amount

    special_chars = "@#$%&_?" # Special characters


    password += (random.choices(string.ascii_uppercase, k = uppercase_amount)) # Add the uppercase characters
    password += (random.choices(string.digits, k = random_num_amount)) # Add the numbers
    password += (random.choices(string.ascii_lowercase, k = lowercase_amount)) # Add the lowercase characters
    password += (random.choices(special_chars, k = 3)) # Add the special characters


    # Make a new password when the password is not valid
    while not password_position:
        first_three_rule = True # If there is not a number on the first 3 positions

        random.shuffle(password) # Shuffles the password

        # Check if there is not a number on the first 3 positions
        for character in password[:3]:
            if character.isnumeric():
                first_three_rule = False
                break      

        else:
            # Check if the special chars are not on a specific position 
            if first_three_rule and not password[0] in special_chars and not password[-1] in special_chars:
                password_position = True    

    # Returns the password
    else:
        password = ''.join(password)
        return password


password = generate_random_password(24) # Make the password with the length that is given

print(password)