from random import shuffle 


def make_deck():    
    colors = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'boer', 'vrouw', 'heer', 'aas']
    cards = ['harten', 'klaveren', 'schoppen', 'ruiten']
    deck = []

    # Add the cards to the deck
    for card in cards:
        for color in colors:
            deck.append(card + ' ' + color)

    # Add the jokers to the deck
    for i in range(0, 2):
        deck.append("joker")

    shuffle(deck) # Shuffles the deck


    return deck # Returns the deck

def show_deck(deck):
    # Print the first 7 cards 
    for num in range(1, 8):
        card = deck[num - 1]
        card_info = "kaart {}: {}".format(num, card)
        print(card_info)
    else:   
        # Print the whole deck
        print()
        print(deck)


deck = make_deck() # Makes the deck
show_deck(deck) # Show the deck