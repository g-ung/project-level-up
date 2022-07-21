#! python 3
'''
Convert ISO 8601 and US Date Format to DD-MM-YYYY

Use regular expressions to find date that are in 
ISO 8601/US date pattern, then converts them to 
DD/MM/YYYY or DD/MM/YY format
'''

import re, fileinput
from datetime import datetime

def main():
    filename = "date.txt"

    # open a file, use findall() to find matches
    with fileinput.FileInput(filename, inplace=True, backup='.bak') as f:

        # ISO date regex
        iso_date_regex = re.compile(r'''(
            (\d{4})                    # year in YYYY format
            (\.|-|\/)                  # separator
            (0[1-9]|1[0-2])            # month in MM format
            (\.|-|\/)                  # separator
            (0[1-9]|[12][0-9]|3[01])   # day in DD format
            )''', re.VERBOSE)
        
        # ISO basic date format regex
        iso_date_basic = re.compile(r'''(
            (\d{4})                      # year in YYYY format
            (0?[1-9]|1[0-2])             # month in MM format
            (0?[1-9]|[12][0-9]|3[01])    # day in DD format
            )''', re.VERBOSE)

        # US date regex
        us_date = re.compile(r'''(
            (0[1-9]|1[0-2])            # month in MMformat
            (\.|-|\/)                  # separator
            (0[1-9]|[12][0-9]|[01])    # day in DD format
            (\.|-|\/)                  # separator
            (\d{2,4})                  # year in YY or YYYY format
            )''', re.VERBOSE)
        
        for line in f:
            line = line.strip() # data clean up by removing leadding and trailing chars.
            date_obj = None
            if re.findall(iso_date_regex, line):
                date_obj = datetime.strptime(line, '%Y-%m-%d') # why is %d is a different colour than the rest of the format?


            
        # regex test
        #mo1 = iso_date_regex.findall("This is an iso date variants: 2022/07/19, 2022-07-20, 2022/7/3, 20220808, 202296")
        #print(mo1)
        #mo2 = iso_date_basic.findall("This is an iso date variants: 2022/07/19, 2022-07-20, 2022/7/3, 20220808, 202296")
        #print(mo2)

        #mo3 = iso_date_regex.findall(content)
        #print(mo3)
        #mo4 = iso_date_basic.findall(content)
        #print(mo4)


if __name__ == '__main__':
    main()