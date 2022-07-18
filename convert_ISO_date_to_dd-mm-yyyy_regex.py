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
        content = f.read()
        matches = []

        # ISO date regex
        iso_date_regex = re.compile(r'''(
            ^(\d{4})                         # year in YYYY format
            (\/|-)                           # separator
            (\d{2}(0[1-9]|1[0-2]))           # month in MM format
            (\/|-)                           # separator
            (\d{2}(0[1-9]|[12][0-9]|3[01])$  # day in DD format
            )''', re.VERBOSE)

        # ISO basic format date regex, YYYYMMDD
        basic_isodate = re.compile(r'''(
            ^(\d{4})
            (0[1-9]|1[0-2])
            (0[1-9]|[12][0-9]|3[01])$
            )''', re.VERBOSE)
        
        # use findall() to match ISO date regex pattern in file
        for groups in iso_date_regex.findall(content):
            convert_date = ' '.join([groups[5], groups[3], groups[1]])
            if groups != '':
                convert_date += groups[6]
            matches.append(groups[0])
        
        if len(matches) > 0:
            print("Converted ISO dates to dd-mm-yyyy")
            print('\n'.join(matches))
        

if __name__ == '__main__':
    main()