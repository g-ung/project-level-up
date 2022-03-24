# AI Porgamming with Python: Lesson 6 Scripting, Module 31: Practice Question

# Create a function that opens the flowers.txt, reads every line in it, and saves it as a dictionary. 
# The main (separate) function should take user input (user's first name and last name) and parse the 
# user input to identify the first letter of the first name. It should then use it to print the flower 
# name with the same first letter (from dictionary created in the first function).

#  Write your code here

# HINT: create a dictionary from flowers.txt

# HINT: create a function to ask for user's first and last name
# function: builds flower_dict from file: flowers.txt
def name_flower_dict(filename):
    flower_dict = {}
    with open('/Users/gabe_ung/Desktop/flowers.txt', 'r') as f: # open file: flowers.txt
        for line in f:
            letter, flower = line.strip().lower().split(':') # split the line where there is a ':'
            flower_dict[letter] = flower.strip() # build dictionary with key (letter), value (flower) from file: flowers.txt
    return flower_dict

# main function: prompts user for input, parses the first letter of their name
# this function also calls name_flower_dict function to create the dictionary
def main():
    the_flower_dict = name_flower_dict('/Users/gabe_ung/Desktop/flowers.txt')
    full_name = input("Please enter your first [space] last name only: ")
    first_name = full_name[0].lower()
    first_letter = first_name[0]
    # prints output from user with value for corresponding key (letter) in flower_dict dictionary
    print("Unique flower name with the first letter: {}".format(the_flower_dict[first_letter]))
main()

# print the desired output
# check with print
# print(flower_dict)
