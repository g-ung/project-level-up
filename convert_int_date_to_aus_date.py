#! python 3
'''
Convert International Date Formate to Australian Date Format
Use regular expressions to finds date that are in 
international format and converts them to Australian format
'''

import re

def main():
    # open a file, use findall() to find matches
    with open("/Users/gabe_ung/Desktop/date.txt", 'r') as f:
        matches = [] # empty list to store matches
        content = f.read()

        # international date regex
        intl_date_regex = re.compile(r'''(
            (^\d{4})                            # year in YYYY format
            (\/|-|\.)                           # separator
            (\d{2}(0[1-9]|1[0-2]))              # month in MM format
            (\/|-|\.)                           # separator
            (\d{2}(0[1-9]|[12][0-9]|3[01])$)    # day in DD format
            )''', re.VERBOSE)
        
        # use findall() to match intl. date regex pattern in file
        for groups in intl_date_regex.findall(content):
            convert_date = '-'.join([groups[5], groups[3], groups[1]])
            if groups[6] != '':
                convert_date += groups[6]
            matches.append(groups[0])
    
        if len(matches) > 0:
            print("Dates found and converted:")
            print('\n'.join(matches))
        else:
            print("No dates fround")

if __name__ == '__main__':
    main()