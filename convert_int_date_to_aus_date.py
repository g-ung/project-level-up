#! python 3
'''
Convert International Date Formate to Australian Date Format
Finds date that are in international format and converts them
to Australian format
'''

import re

def main():
    # international date regex
    intl_date_regex = re.compile(r'''(
        (\d{4})             # year in YYYY format
        (\\|-|\.)           # separator
        (\d{2})             # month in MM format
        (\\|-|\.)           # separator
        (\d{2})             # day in DD format
    )''', re.VERBOSE)

    # TODO: code open file to run search
    with open('text.txt') as f:
        matches = [] # empty list to store matches

        for groups in intl_date_regex.findall(f):
            convert_date = '-'.join([groups[5], groups[3], groups[1]])
            if groups[6] != '':
                convert_date += ' x' + groups[6]
            matches.append(groups[0])
        if len(matches) > 0:
            

    

if __name__ == '__main__':
    main()