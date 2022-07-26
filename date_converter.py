#! python 3
'''
Convert ISO 8601 and US Date Format to DD-MM-YYYY

Use regular expressions to find date that are in 
ISO 8601/US date pattern, then converts them to 
DD/MM/YYYY or DD/MM/YY format
'''

import re, fileinput
from datetime import datetime

def lookup(dates):

    patterns = {
            '%Y/%m/%d': r'^\s*\d{4}\/\d{1,2}\/\d{1,2}\s*$',
            '%m/%d/%Y': r'^\s*\d{1,2}\/\d{1,2}\/\d{4}\s*$',
            '%Y-%m-%d': r'^\s*\d{2,4}-\d{1,2}-\d{1,2}\s*$',
            '%m-%d-%Y': r'^\s*\d{1,2}-\d{1,2}-\d{4}\s*$',
            '%m-%d-%y': r'^\s*\d{1,2}-\d{1,2}-\d{2}\s*$',
            '%m/%d/%y': r'^\s*\d{1,2}\/\d{1,2}\/\d{2}\s*$',
            '%Y%m%d': r'^\s*\d{4}\d{1,2}\d{1,2}\s*$'
            }
    desired_dt_format = '%d/%m/%Y'
    
    # test
    #filepath = "/Users/gabe_ung/Desktop/date.txt"
    # open a file, use findall() to find matches
    #with fileinput.FileInput(filepath, inplace=True, backup='.bak') as f:
    try:
        for dt_format, pattern in patterns.items():
            if re.findall(pattern, dates):
                return "CONVERTED", datetime.strptime(dates, dt_format).strftime(desired_dt_format)
    except Exception as e:
        return "EXCEPTION", datetime.now().replace(microsecond=0, second=0, minute=0, hour=0)
    return "NOT CONVERTED", datetime.now().replace(microsecond=0, second=0, minute=0, hour=0)
   
def main():
    # place holder for .txt/.CSV file
    test_dates = ['2022/07/18', '2022-07-19', '2022/7/18', '2022.7.18', '20220803', '20210603', '202292', '2022903', '2022-07-21T02:10:46Z', '07/01/22', '08/01/2022', '08-21-2021']

    for date in test_dates:
        status, date_obj = lookup(date)
        print("Input Date: [{}] [{}] to [{}]".format(date, status, date_obj))

    #dt = datetime.strptime('2022/12/21', '%Y/%m/%d').strftime(desired_dt_format)
    #print(dt)

if __name__ == '__main__':
    main()