'''
Table Printer
REQUIREMENTS:
1. Take the list of lists of strings and display it a well-organised table
2. Each column need to be right-justified
3. Your print_table() would print the table in the following format:

  apples Alice   dog
 oranges   Bob  cats
cherries Carol moose
  banana David goose

NOTE: Assume that all the innner lists will contain the same number of strings
'''
def print_table(table):
    col_widths = [0] * len(table) # create a list containing the same no. of 0 values as there are no. of inner lists in table_data

    # find the longest string in nested list table (table_data)
    for x_axis in range(len(table)): # iterate through len() of table to access the index, i.e. 0, 1, 2
        # check with
        # print(i)
        for y_axis in table[x_axis]: # iterate through the first list, index 0, of table to access the list in position 0
            # check with
            # print(j)
            '''
            Compare the length of the item (string) in col_widths in index x_axis with 
            the item (string) in the first list in table.  If col_widths[x_axis] < len(y_axis)
            update with len(y_axis) as longest string
            '''
            if col_widths[x_axis] < len(y_axis): 
                col_widths[x_axis] = len(y_axis)
                # check with
                # print(col_widths[x_axis])
    
    # transpose the nested list and print the table
    '''
    for i in range(len(table[0])): # not a fan of this method
        # print(i)
        for j in range(len(table)):
            # print(j)
            print(table[j][i].rjust(col_widths[j]), end=' ') # print table with rjust() proportionate to the longest word in each col_widths
        print()
        i += 1
    '''
    for i in zip(*table):
        # print(i)
        transposed_list = list(i)
        # this prints the correct format but would prefer not to hard code the rjust() values
        print(transposed_list[0].rjust(8), transposed_list[1].rjust(5), transposed_list[2].rjust(5))

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)