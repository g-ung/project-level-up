import random

num_of_streaks = 0
streak_count = 0
heads = 0
tails = 0
flip_list = []

for sample_size in range(10000):
    # Code that creates a list of 100 'heads or 'tails' values.
    for i in range(100):
        if random.randint(0,1) == 1:
            flip_list.append('H')
            heads += 1
        if heads == 6:
            streak_count += 1
    else:
        flip_list.append('T')
        tails += 1
        if tails == 6:
            streak_count += 1
# Code that checks if there is a streak of 6 heads or tails in a row.
    if streak_count == 6:
        num_of_streaks += 1
  
print('Chance of streak: %s%%' % (num_of_streaks / 100))