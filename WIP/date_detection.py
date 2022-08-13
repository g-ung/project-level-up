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
1-28 all months

29 for Feb in leap year, divisible by 4 and divisible by 400,
excpt for century divisble by 100:
century % 4 == 0
century % 400 == 0
century % 100 != 0
'''
import re

def date_validator(input_date):
    # date regex pattern for dd/mm/yyy, this regex does not do any date validation
    dt_pattern = re.compile(r'''(
            (\d{1,2})           # day, will accept invalid days e.g. 51/03/2000
            /                   # separator
            (\d{1,2})           # month
            /                   # separator
            ([12]\d{3})         # year 1000-2999
            )''', re.VERBOSE)
    
    # date matching
    dt_validation = dt_pattern.findall(input_date)

    # date variables
    # months with 30 days
    months_30 = [4, 6, 9, 11]
    
    for groups in dt_validation: # date validation check
        # validate months with 30 days
        '''
        Use membership operator 'in' validate months with 30 days
        REFERENCE:
        https://www.programiz.com/python-programming/operators
        '''
        if groups[3] in months_30 and groups[1] == 31: 
            print("Valid. {} is a valid date!".format(input_date))
        # validate leap year
        elif groups[3] == 2 and groups[1] == 29:
            # define condition for a leap year
            if (groups[5] % 4 == 0 and groups[5] % 100 != 0) or (groups[5] % 400 == 0 and groups[5] % 100 != 0):
               print("Valid. {} is a valid date!".format(input_date))
        elif groups[3] not in months_30 and groups[1] <= 31: # check months with 31 days
            print("Valid. {} is a valid date!".format(input_date))
        else:
            print("Valid. {} is a valid date!".format(input_date))

def main():
    date_validator(input("Please enter date in DD/MM/YYYY: "))

if __name__ == '__main__':
    main()