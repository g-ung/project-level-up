# AI Porgamming with Python: Lesson 4 Control Flow, Module 26: Check For Understanding: For and While Loops
# Question: What type of loop should we use?

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

odd_num_count = 0 # Tracks no. of odd numbers
sum_odd_num = 0 # Add odd numbers stored here
index = 0 # Access elements in num_list
len_num_list = len(num_list) # Lets me access the index of num_list, should give me int 25

while (odd_num_count < 5) and (index < len_num_list): # Condition True when no. of odd nos. < 5 and keep checking until iterate to end of num_list
    if num_list[index] % 2 != 0: # Odd no. check
        sum_odd_num += num_list[index] # Adds odd nos. in num_list
        odd_num_count += 1 # Tracking no. of odd nos. > then is check agains while loop condition
    index += 1 # Moves to next element incrementally to next element in num_list
    
print("{} odd numers were added".format(odd_num_count))
print("Total of odd numnbers added: {}".format(sum_odd_num))
