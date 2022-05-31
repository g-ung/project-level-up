'''
List to Dictionary Function for Fantasy Game Inventory
REQUIREMENTS:
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
You will need to include the function you wrote for the previous 
program: fantasy_game_inventory.py in this script

NOTE: The inflect package a third-party pacakage. If you want to 
install the inflect package I recommend you create a virtual 
environment then pip install the inflect package in the virtual 
environment so it doesn't mess with the built in libraries in Python.

For macOS/Linux CLI: 
>> python3 -m venv <venv name> # command to create your virtual environment
>> source <venv name>\bin\activate # command to activate your virtual environment
>> deactivate # deactivate your virtual environment

To delete your virtual environment simply delete the folder in Finder or 
in terminal

For macOS/Linux
>> rm -rf <venv name> # command to delete your virtual environment
'''
#import inflect

def add_to_inventory(inventory, added_items):
    for item in added_items: # dragon_loot argument passed as a parameter to add_items then iterate through the list
        '''
        If a key does not yet exist the inventory dictionary, arguement current_inv passed as parameter
        to inventory, get() will return value 0 and inventory[item] is set to 1. When the iteration
        encounters another item that already exist in the dictionary the value of the key is 1++, i.e.
        the 2nd encounter of 'gold coin' key the value would be 1++ resulting in a count of 2
        REFERENCE:
        https://www.programiz.com/python-programming/methods/dictionary/get
        '''
        inventory[item] = inventory.get(item, 0) + 1
    
    return inventory # use explicity return statement to return inventory so it can be passed to the function add_to_inventory

def display_inventory(inventory):
    item_count = 0 # variable to store total number of items in iventory, i.e. the values in the dictionary
    print("Inventory:")
    
    for key, value in inventory.items(): # use items() to iterate through inventory dictionary
        print("{} {}".format(value, key)) 
        item_count += value # update item_count with value, int, in dictionary
        #if value == 1:
        #    key = p.singular_noun(key, value)
        #else:
        #    key = p.plural(key, value)
           
    print("Total number of items: {}".format(item_count))

def main():
    #p = inflect.engine()    
    current_inv = {'gold coin': 42, 'rope': 1}
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

    current_inv = add_to_inventory(current_inv, dragon_loot)
    display_inventory(current_inv)

if __name__ == '__main__':
    main()