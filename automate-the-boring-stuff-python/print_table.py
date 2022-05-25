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
    for i in range(len(table)): # iterate through table as range(len(table)) to access the nested list as indexes
        for j in table[i]: # iterate through table index, i.e. each word/string, to find the longest string by length
            if col_widths[i] < len(j):
                col_widths[i] = len(j)
    print(table)

table_data = [['apples', 'oranges', 'cherries', 'banana'], 
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)