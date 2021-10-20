def add_groceries():

    items = {}
    add_items = True

    while add_items:
        item = input('Wat wilt u toevoegen aan uw boodschappen lijstje? (zeg "stop" als u wilt stoppen met het toevoegen van boodschappen): ')

        try:
            if item != "stop":
                items[item] += 1

        except KeyError: 
            items[item] = 1

        finally: 
            if item == "stop":
                add_items = False

    else:
        return items


groceries = add_groceries()

print(groceries)