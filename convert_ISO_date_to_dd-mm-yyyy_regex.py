#! python 3
'''
Convert ISO Date Format to Australian Date Format
Use regular expressions to find date that are in 
ISO format and converts them to DD/MM/YYYY format
'''

import re

def main():
    # open a file, use findall() to find matches
    with open("/Users/gabe_ung/Desktop/date.txt", 'r') as f:
        content = f.read()

        # ISO date regex
        iso_date_regex = re.compile(r'''(
            (\d{4})                     # year in YYYY format
            (\.|-|\/)                   # separator
            (0?[1-9]|1[0-2])            # month in MM format
            (\.|-|\/)                   # separator
            (0?[1-9]|[12][0-9]|3[01])   # day in DD format
            )''', re.VERBOSE)
        
        # ISO basic date format regex
        iso_date_basic = re.compile(r'''(
            (\d{4})                      # year in YYYY format
            (0?[1-9]|1[0-2])             # month in MM format
            (0?[1-9]|[12][0-9]|3[01])    # day in DD format
            )''', re.VERBOSE)

        # regex test
        #mo1 = iso_date_regex.findall("This is an iso date variants: 2022/07/19, 2022-07-20, 2022/7/3, 20220808, 202296")
        #print(mo1)
        #mo2 = iso_date_basic.findall("This is an iso date variants: 2022/07/19, 2022-07-20, 2022/7/3, 20220808, 202296")
        #print(mo2)

        mo3 = iso_date_regex.findall(content)
        print(mo3)
        mo4 = iso_date_basic.findall(content)
        print(mo4)


if __name__ == '__main__':
    main()