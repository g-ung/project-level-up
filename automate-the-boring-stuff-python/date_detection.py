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
    # date regex pattern for dd/mm/yyyy, this regex does not do any date validation as per requirements
    dt_pattern = re.compile(r'([12][0-9]|3[0-1]|0?[1-9])/(1[0-2]|0?[1-9])/([12]\d{3})')
     
    # date matching
    dt_validation = dt_pattern.findall(input_date)

    # months with 30 & 31 days
    months_30 = [4, 6, 9, 11]
    month_31 = [2, 4, 6, 9, 11]
    for day, month, century in dt_validation: # date validation check
        # validate months with 30 and 31 days
        '''
        Use membership operator 'in' and 'not in' validate months with 30 & 31 days
        REFERENCE:
        https://www.programiz.com/python-programming/operators
        '''
        day = int(day)
        month = int(month)
        century = int(century)
        if month in months_30 and day < 31 or (month not in month_31):
            print("Valid. {} is a valid date!".format(input_date)) 
        # validate leap year
        elif month == 2 and day == 29 and century % 4 == 0 and (century % 100 != 0 or century % 400 == 0) or (month == 2 and day < 29):
            print("Valid. {} is a valid date!".format(input_date))
        else:
            print("Invalid. {} is not a valid date!".format(input_date))
            
def main():
    date_validator(input("Please enter date in DD/MM/YYYY: "))

if __name__ == '__main__':
    main()