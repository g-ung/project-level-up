import random

num_of_streaks = 0
streak_count = 0


for sample_size in range(10000):
    # Code that creates a list of 100 'heads or 'tails' values.
    flip_list = [] # empty list to store no. heads/tails
    for i in range(100):
        if random.randint(0,1) == 1: # if 1 it is heads, append() 'H' to some_list
            flip_list.append('H')
        else: # if 0 it is tails, append() 'T' to some_list
            flip_list.append('T')
# Code that checks if there is a streak of 6 heads or tails in a row.
    for index, item in enumerate(flip_list):
        '''
        Could use for i in range(len(some_list)) to access the index in loop
        variable i enumerate returns an iterable with index
        REFERENCE:
        https://www.programiz.com/python-programming/methods/built-in/enumerate
        '''
        if index == 0: # in postion 0 do nothing
            pass
        elif flip_list[index] == flip_list[index-1]:
            '''
            This block of code checks if preceeding item with proceeding item in 
            list value are equal, i.e. the same either heads or tails.  For each 
            matching item streak_count is incremented by 1, 6 streak_counts 
            counts as 1 num_of_streaks, i.e. total streak count
            '''
            streak_count += 1
        else: # if no match found steak_count is set to 0
            streak_count = 0
        
        if streak_count == 6: # when a streak_count == 6 num_of_streaks is incremented by 1
            num_of_streaks += 1
             
print("Chance of streak: {}%".format(num_of_streaks / 100))