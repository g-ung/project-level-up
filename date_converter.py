#! python 3
'''
Convert ISO 8601 and US Date Format to DD-MM-YYYY

Use regular expressions to find date that are in 
ISO 8601/US date pattern, then converts them to 
DD/MM/YYYY or DD/MM/YY format
'''

import re
from datetime import datetime

def lookup(dates):
    # define regex patterns
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
        (0[1-9]|1[0-2])             # month in MM format
        (0[1-9]|[12][0-9]|3[01])    # day in DD format
        )''', re.VERBOSE)

    # US date regex
    us_date = re.compile(r'''(
        (0[1-9]|1[0-2])            # month in MMformat
        (\.|-|\/)                  # separator
        (0[1-9]|[12][0-9]|3[01])    # day in DD format
        (\.|-|\/)                  # separator
        (\d{2,4})                  # year in YY or YYYY format
        )''', re.VERBOSE)    
    
    desired_dt_format = '%d/%m/%Y'

    patterns = {'%Y/%m/%d': iso_date_regex,
                '%Y-%m-%d': iso_date_regex,
                '%Y%m%d': iso_date_basic,
                '%m/%d/%Y': us_date,
                '%m-%d-%Y': us_date,
                '%m/%d/%y': us_date,
                '%m-%d-%y': us_date
                }
    
    #filepath = "/Users/gabe_ung/Desktop/date.txt"
    # open a file, use findall() to find matches
    #with fileinput.FileInput(filepath, inplace=True, backup='.bak') as f:
    try:
        for dt_format, pattern in patterns.items():
            if re.match(pattern, dates):
                return "CONVERTED", datetime.strptime(dates, dt_format).strftime(desired_dt_format)
    except Exception as e:
        return "EXCEPTION", datetime.now().replace(microsecond=0, second=0, minute=0, hour=0)
    return "NOT CONVERTED", datetime.now().replace(microsecond=0, second=0, minute=0, hour=0)
   
def main():
    # place holder for .txt/.CSV file
    test_dates = ['2022/07/18', '2022-07-18', '2022/7/18', '2022.7.18', '20220803', '20210603','202292', '2022903', '2022-07-21T02:10:46Z', '07/01/22', '08/01/2022', '08-21-21']

    for date in test_dates:
        status, date_obj = lookup(date)
        print(f'Input Date: [{date}] [{status}] to [{date_obj}]')
    
    #dt = datetime.strptime('2022/12/21', '%Y/%m/%d').strftime(desired_dt_format)
    #print(dt)

if __name__ == '__main__':
    main()