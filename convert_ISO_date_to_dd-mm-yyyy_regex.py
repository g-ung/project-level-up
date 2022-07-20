#! python 3
'''
Convert ISO Date Format to Australian Date Format
Use regular expressions to find date that are in 
ISO format and converts them to DD/MM/YYYY format
'''

import re

def main():
    # open a file, use findall() to find matches
    #with open("/Users/gabe_ung/Desktop/date.txt", 'r') as f:
        #content = f.read()

        # ISO date regex
        iso_date_regex = re.compile(r'''(
            (\d{4})                     # year in YYYY format
            (\.|-|\/)                   # separator
            (0?[1-9]|1[0-2])             # month in MM format
            (\.|-|\/)                   # separator
            (0?[1-9]|[12][0-9]|3[01])    # day in DD format
            )''', re.VERBOSE)
        
        # ISO basic date format regex
        iso_date_basic = re.compile(r'''(
            (\d{4})                     # year in YYYY format
            (0?[1-9]|1[0-2])             # month in MM format
            (0?[1-9]|[12][0-9]|3[01])    # day in DD format
            )''', re.VERBOSE)

        # regex test
        string = "This is an iso date: 2022/07/19, 2022-07-20, 2022/7/3"

        result = re.sub(iso_date_regex, '\\3-\\2-\\1', string, re.VERBOSE)
        print(result)


if __name__ == '__main__':
    main()