'''
List to Dictionary Function for Fantasy Game Inventory
REQUIREMMENTS:
1. Write a function named add_to_inventory(inventory, added_items), where the "inventory"
parameter is the dictionary representing the player's inventory and the "added_items" 
parameter is the list like dragon_loot
2. the add_to_inventory() function should return a dictionary that represents the updated
inventory
3. Expected output:

Inventory:
45 gold coin
1 rope
1 ruby
1 dagger
Total number of items: 48

NOTE: The added_items list can contain multiples of the same item.
NOTE: You will need to include the function you wrote for the previous 
program: fantasy_game_inventory.py in this script

'''
def add_to_inventory(inventory, added_items):
    for item in added_items: # dragon_loot argument parsed in as a parameter to add_items then iterate through the list
        '''
        If a key does not yet exist the inventory dictionary, arguement current_inv pasrsed as parameter
        to inventory, get() will return value 0 and inventory[item] will be set to 1. When the iteration
        encounters another item that already exist in the dictionary the value of the key is 1++, i.e.
        the 2nd encounter of 'gold coin' key the value would be 1++ resulting in 2
        REFERENCE:
        https://www.programiz.com/python-programming/methods/dictionary/get
        '''
        inventory[item] = inventory.get(item, 0) + 1
    
    return inventory # use explicity return statement to return inventory so it can be parsed into the function add_to_inventory

def display_inventory(inventory):
    item_count = 0 # variable to store total number of items in iventory, i.e. the values in the dictionary
    print("Inventory:")
    
    for key, value in inventory.items(): # use items() to iterate through inventory dictionary
        print("{} {}".format(value, key)) 
        item_count += value # update item_count with value, int, in dictionary
    
    print("Total number of items: {}".format(item_count))
    
current_inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

current_inv = add_to_inventory(current_inv, dragon_loot)
display_inventory(current_inv)
