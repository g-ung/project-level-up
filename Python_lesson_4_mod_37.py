# AI Porgamming with Python: Lesson 4 Control Flow, Module 37: List Comprehension: Extract First Names; Multiple of 3s; Filter Names by Scores
## extract first names
## 
from multiprocessing.sharedctypes import Value


names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names] # us split method to split loop variable name starting with index 0, i.e. name.split()[0] >>> split 'Rick Sanchez'
print(first_names)

## the for loop version
first_names_1 = [] # create an empty list so so you can use the append() method to add to the list
for name in names: # loop variable name is napped to names in names list
    
    first_names_1.append(name.split()[0].lower()) # for each name starting at index 0 split() and lower() and add to first_names_1 list

print("\n", first_names_1)

## multiples of threes, create a list multiple_3 containing the first 20 multiples of 3
multiple_3 = [num * 3 for num in range(1, 21)]
print(multiple_3)

## the for loop version
the_other_multiple_3 =[] # empty list to store multiple of 3 list to be generated
for num in range(1, 21): # create a num from 1 to 20
    the_other_multiple_3.append(num * 3) # for each num * 3 from 1 to 21 add to the_other_multiple_3 list
print("\n", the_other_multiple_3)

## filter names by scores, create list of names passed that only include those that scoreed at least 65
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          } # dictionary of keys: names, values: score, i.e. Rick Sanchez: 70

# use items() function to access the scores from value: score 
# b/c dictionaries have two elements: keys and values we only want to iterate through the key: name of the dictionary, thence 'name for name'
# check only scores that are >= 65 in value: score of dictionary
passed = [name for name, score in scores.items() if score >= 65] 
print("\n", passed)

## for loop version
you_passed = []
for key, value in scores.items():
    if  value >= 65:
        you_passed.append(key)
print("\n", you_passed)
