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
    col_width = [0] * len(table)
    
    for list in table:
        for string in list:
            index = 0
            if len(string) > len(col_width[index]):
                col_width[index] = len(string)
                index += 1

    print(col_width)

table_data = [['apples', 'oranges', 'cherries', 'banana'], 
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)