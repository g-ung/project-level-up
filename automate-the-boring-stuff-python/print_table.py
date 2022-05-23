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

NOTE: Assum that all the innner lists will contain the same number of strings
'''
def print_table(table):
    col_widths = [0] * len(table) # create a list containing the same no. of 0 values as there are no. of inner lists in tabel_data
    
    for list in table: 
        '''
        Iterate through table to access the nested lists to find the longest string 
        and store that value to col_width[index]
        '''
        index = 0
        if len(list) > len(col_widths[index]):
            col_widths[index] = len(list)
            index += 1
        for string in :
            

    print(col_width)

table_data = [['apples', 'oranges', 'cherries', 'banana'], 
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)