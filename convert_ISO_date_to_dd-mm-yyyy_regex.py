#! python 3
'''
Convert ISO Date Format to Australian Date Format
Use regular expressions to finds date that are in 
ISO format and converts them to DD/MM/YYYY format
'''

import re

def main():
    # open a file, use findall() to find matches
    with open("/Users/gabe_ung/Desktop/date.txt", 'r') as f:
        content = f.readlines()

        # ISO date regex
        iso_date_regex = re.compile(r'''(
            ^(\d{4})                            # year in YYYY format
            (\.|-|/)                            # separator
            (\d{2}(0[1-9]|1[0-2]))              # month in MM format
            (\.|-|/)                            # separator
            (\d{2}(0[1-9]|[12][0-9]|3[01]))$    # day in DD format
            )''', re.VERBOSE)
        
        # ISO basic date format regex
        iso_date_basic = re.compile(r'''(
            ^(\d{4})                            # year in YYYY format
            (\d{2}(0[1-9]|1[0-2]))              # month in MM format
            (\d{2}(0[1-9]|[12][0-9]|3[01]))$    # day in DD format
            )''', re.VERBOSE)
        
        

if __name__ == '__main__':
    main()