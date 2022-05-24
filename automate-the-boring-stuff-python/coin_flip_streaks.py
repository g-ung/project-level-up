'''
Coin Flip Streaks
REQUIREMENTS:
1. Generate a list of randomly selected 'heads and 'tails' values
2. Check if there is a streak of six 'heads' or 'tails' in it
3. Put the code in a loop that repeats 10,000 times (this is the sample size)
4. Calculate the percentage of coin flips that contain a streak of six heads or tails
'''
import random

num_of_streaks = 0
streak_count = 0


for sample_size in range(10000):
    # Code that creates a list of 100 'heads or 'tails' values.
    flip_list = [] # empty list to store no. heads/tails; reset list after each 100 cycles
    for i in range(100):
        if random.randint(0,1) == 1: # if 1 it is heads, append() 'H' to some_list
            flip_list.append('H')
        else: # if 0 it is tails, append() 'T' to some_list
            flip_list.append('T')
# Code that checks if there is a streak of 6 heads or tails in a row.
    for index, item in enumerate(flip_list):
        '''
        Use enumerate to returns an iterable with index to access items in
        flip_list
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