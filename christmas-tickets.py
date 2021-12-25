from random import choice


# Ask the user all the names
def get_names():
    names = []

    choosing_names = True


    # If the user is choosing names
    while choosing_names:
        name = input("Kies een naam om toe te voegen (als je wilt stoppen typ 'stop'): ")

        # If the user typed 'stop'
        if name == 'stop':
            # If the user chose already 2 names
            if len(names) >= 2:
                choosing_names = False # Stop the question
        
            # If the user did not chose already 2 names
            else:
                print("U moet meer dan 2 spelers hebben toegevoegd om te stoppen") # Error message
        else:
            # If the name is not already chosen
            if name not in names:
                names.append(name) # Add the name to the list
        
            # If the name is already chosen
            else:
                print(f"De naam {name} is al gekozen", end="\n") # Error message

    # If the user did not want to add more names
    else:
        return names # Return all the names


# Give a person another person to make a christmas present
def get_tickets(names):
    tickets = {}

    # For every name the user added
    for name in names:
        random_name_choosing = True

        # While the random name is the same as the persons name
        while random_name_choosing:
            random_name = choice(names)

            if random_name != name:
                tickets[name] = random_name
                random_name_choosing = False


    return tickets # Return the dictionary with all the persons and the person he got


# Show which person got who
def show_tickets(tickets):
    # For every person
    for person in tickets:
        print(f"persoon genaamd '{person}' heeft het lot van de persoon genaamd '{tickets[person]}' getrokken ")


# Call all the functions
def main():
    names = get_names() # Ask all the names
    tickets = get_tickets(names) # Give the persons another persons ticket
    show_tickets(tickets) # Show the persons the persons got




# When the program starts
if __name__ == "__main__":
    main()