#! python 3
'''
Date Detection
REQUIREMENTS
1. Detect date formate: DD/MM/YYYY
2. Store date data into string variables: month, day, and year
3. The code should detect if a date is valid
4. The code should detect if a year is a leap year

Assumptions:
1. Day range from 01 to 31
2. Month range from 01 to 12
3. Year range from 1000 to 2999

NOTE:
The regular expression doesn't have to detect for leap year;
it will accept nonexistent dates like 31/02/2020 or 31/04/2021.
i.e. the regex does not do any date validation.

Write additional code to validate correct dates.

If a day or month is a single digit it'll have a leading zero.

Days
31 for Jan, Mar, May, Jul, Aug, Oct, Dec
30 for Apr, Jun, Sep, Nov
29-30 for Jan, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov Dec
29 for Feb in leap year, divisible by 4 and divisible by 400,
excpt for century divisble by 100
1-28 all months
'''

import re

def main():
    # test dates, ph for user input dates
    sample_dates = ['21/03/2000', '31/02/2020', '29/02/2000', '3/06/2021', '29/02/2001', '56/3/1999', '4/09/1000', '4/9/2999', '4/09/999'] 
    
    # date regex pattern for dd/mm/yyy
    dt_pattern = re.compile(r'''(
            (\d{1,2})             # day 01-31
            /                     # separator
            (\d{1,2})             # month 01-12
            /                     # separator
            ([12]\d{3})           # year 1000-2999
            )''', re.VERBOSE)
    # test
    for date in sample_dates:
        if re.match(dt_pattern, date):
            print("Format match: {}".format(date))
        else:
            print("Format not match: {}".format(date))
    '''
    # is a leap year
    century % 4 == 0
    century % 400 == 0
    century % 100 != 0
    
    # feb is a leap year
    feb == 2
    days == 29
    days not range(1,31)
    
    # months with 30 days
    months = [4, 6, 9, 11]
    '''




        


if __name__ == '__main__':
    main()