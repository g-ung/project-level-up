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

    transpose = list(zip(*table))
    print(transpose)
    transpose = [list(sublist) for sublist in transpose]
    print(transpose)
    transpose = [' '.join([item for item in sublist]) for sublist in transpose]
    
    
    # check with
    # list_to_string = ' '.join(transpose)
    # print(list_to_string)
    # kinda works, should be able to do a loop to do this for me
    # print(transpose[0].rjust(10), "\n", transpose[1].rjust(10), "\n", transpose[2].rjust(10), "\n", transpose[3].rjust(10))
    # print(transpose)

table_data = [['apples', 'oranges', 'cherries', 'banana'], 
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)