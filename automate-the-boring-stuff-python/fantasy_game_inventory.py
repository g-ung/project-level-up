'''
Fantasy Game Inventory
REQUIREMENTS:
1. Write a function named display_inventory() that would take any possible "inventory"
and display it like the following format:

Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62
'''
def display_inventory(inventory):
    item_count = 0 # variable to store total number of items in iventory, i.e. the values in the dictionary
    print("Inventory:")
    
    for key, value in inventory.items(): # use items() to iterate through inventory dictionary
        print("{} {}".format(value, key)) 
        item_count += value # update item_count with value, int, in dictionary
    
    print("Total number of items: {}".format(item_count))

player_inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

display_inventory(player_inv)


