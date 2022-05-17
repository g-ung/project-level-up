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
'''
def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory[item] = inventory.get(item, 0) + 1
    
current_inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

current_inv = add_to_inventory(current_inv, dragon_loot)
display_inventory(current_inv)
