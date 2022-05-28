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
    # create a list containing the same number of 0 values as the number of innter lists in table
    col_widths = [0] * len(table) 

    # find the longest string in nested list of table and store in col_widths
    count = 0
    while count < len(table): # iterate through nest listed in table
        for string in table[count]: # search trough the string within the sublist of table
            if col_widths[count] < len(string):
                col_widths[count] = len(string)
                # print(col_widths[count])
        count += 1

    # transpose the nested list and print the table with rjust() proportionately to the longest string
    for word in range(len(table[0])):
        for list in range(len(table)):
            print(table[list][word].rjust(col_widths[list]), end=' ')
        print()

    '''
    for i in zip(*table):
        transposed_list = list(i) # list constructor to i, y-axis of transposed table list, to new transposed list
        #print(transposed_list)

        print(transposed_list[0].rjust(8), transposed_list[1].rjust(5), transposed_list[2].rjust(5)) # use index to print each columm transposed_list
    '''
    
table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)