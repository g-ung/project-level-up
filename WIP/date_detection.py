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

def date_validator(input_date):
    # date regex pattern for dd/mm/yyy, this regex does not do any date validation
    dt_pattern = re.compile(r'''(
            (\d{1,2})           # day 01-31 or 1-31, will accept invalid days e.g. 51
            [/-]                # separator
            (\d{1,2})           # month 01-12 or 1-12
            [/-]                # separator
            ([12]\d{3})         # year 1000-2999
            )''', re.VERBOSE)
    
    # date validation
    dt_validation = dt_pattern.match(input_date)

    # date variables
    # months with 30 days
    months_30 = [4, 6, 9, 11]
    
    # is a leap year
    century % 4 == 0
    century % 400 == 0
    century % 100 != 0
    
    # feb is a leap year
    feb == 2
    days == 29
    days not range(1,31)
    
    if dt_validation == None:
        print("No date entry detected")
    else:
        for day, month, century in dt_validation: # date validation check
            day = int(day)
            month = int(month)
            century = int(century)
            # validate months with 30 days
            if month in months_30: 
                if day == 31:
                    print("Invalid date: {} is not a valid date!".format(input_date))
            elif month == 2:


                print("Format match: {}".format(date))
            else:
                print("Format not match: {}".format(date))
    
    
    

def main():
    try: 
        user_input = input("Please enter date in DD/MM?YYY: ")
    except ValueError as e:
        print("Error: Invalid input! {}, date not in valid format: DD/MM/YYY.  Please try again: ".format(e))

    date_validator(user_input)    

if __name__ == '__main__':
    main()