# List of tuple of items
manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)] 

# The code breaks the loop when weight exceeds or reaches the limit
print("METHOD 1")
weight = 0
items = []
for cargo_name, cargo_weight in manifest: # Loop will iterate thru tuple of items in manifest list
    print("current weight: {}".format(weight))
    if weight >= 100: # check current weight if > 100 break will terminate loop
        print("  breaking loop now!")
        break
    else: # If < 100 add item to items list
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight # Add cargo_weight to wight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

# skips an iteration when adding an item would exceed the limit
# breaks the loop if weight is exactly the value of the limit
print("\nMETHOD 2")
weight = 0
items = []
for cargo_name, cargo_weight in manifest: # Loop will iterate thru tuple of items in manifest list
    print("current weight: {}".format(weight))
    if weight >= 100: # check current weight if > 100 break will terminate loop
        print("  breaking from the loop now!")
        break
    elif weight + cargo_weight > 100:
        print("  skipping {} ({})".format(cargo_name, cargo_weight))
        continue # Skip one iteration if weight + cargo_weight > 100
    else: # If cargo_weight and weight (running total) < 100 add item to items list
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight # Add cargo_weight to wight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))