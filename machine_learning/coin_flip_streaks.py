import random

num_of_streaks = 0
streak_count = 0
flip_list = []

for sample_size in range(10000):
    # Code that creates a list of 100 'heads or 'tails' values.
    for i in range(100):
        if random.randint(0,1) == 1:
        flip_list.append('H')  
    else:
        flip_list.append('T')
# Code that checks if there is a streak of 6 heads or tails in a row.
  if streak_count == 6:
    num_of_streaks += 1
  
print('Chance of streak: %s%%' % (num_of_streaks / 100))