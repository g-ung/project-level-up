#! python 3
'''
Convert ISO 8601 and US Date Format to DD-MM-YYYY

Use regular expressions to find date that are in 
ISO 8601/US date pattern, then converts them to 
DD/MM/YYYY or DD/MM/YY format
'''

import re
from datetime import datetime

def main():
    # place holder for .txt/.CSV file
    #test_dates = ['2022/07/18', '2022-07-19', '2022/7/18', '2022.7.18', '20220803', '20210603', '202292', '2022903', '2022-07-21T02:10:46Z', '07/01/22', '08/01/2022', '08-21-2021']
    iso_dt_slash = re.compile(r'^\s*\d{4}\/\d{1,2}\/\d{1,2}\s*$')
    iso_dt_dash = re.compile(r'^\s*\d{2,4}-\d{1,2}-\d{1,2}\s*$')
    iso_dt_basic = re.compile(r'^\s*\d{4}\d{1,2}\d{1,2}\s*$')
    us_dt_slash = re.compile(r'^\s*\d{1,2}\/\d{1,2}\/\d{4}\s*$')
    us_dt_dash = re.compile(r'^\s*\d{1,2}-\d{1,2}-\d{4}\s*$')
    us_dt_slash_yy = re.compile(r'^\s*\d{1,2}\/\d{1,2}\/\d{2}\s*$')
    us_dt_dash_yy = re.compile(r'^\s*\d{1,2}\/\d{1,2}\/\d{2}\s*$')

    desired_dt_format = '%d/%m/%Y'

    patterns = {
            '%Y/%m/%d': iso_dt_slash,
            '%Y-%m-%d': iso_dt_dash,
            '%m/%d/%Y': us_dt_slash,
            '%m-%d-%Y': us_dt_dash,
            '%m-%d-%y': us_dt_slash_yy,
            '%m/%d/%y': us_dt_dash_yy,
            '%Y%m%d': iso_dt_basic
            }
    input_file = "/Users/gabe_ung/Desktop/dates.txt"
    output_file = "/Users/gabe_ung/Desktop/converted_dates.txt"
    with open(input_file, 'r') as in_f, open(output_file, 'w') as out_f:
        for line in in_f.readlines():
            line = line.strip()

        for dt_format, pattern in patterns.items():
            dt_obj = None
            if re.match(pattern, line):                
                dt_obj = datetime.strptime(line, dt_format)
        out_f.write(dt_obj.strftime(desired_dt_format) + '\n')
    




'''
def date_convert(input):
    iso_dt_slash = re.compile(r'^\s*\d{4}\/\d{1,2}\/\d{1,2}\s*$')
    iso_dt_dash = re.compile(r'^\s*\d{2,4}-\d{1,2}-\d{1,2}\s*$')
    iso_dt_basic = re.compile(r'^\s*\d{4}\d{1,2}\d{1,2}\s*$')
    us_dt_slash = re.compile(r'^\s*\d{1,2}\/\d{1,2}\/\d{4}\s*$')
    us_dt_dash = re.compile(r'^\s*\d{1,2}-\d{1,2}-\d{4}\s*$')
    us_dt_slash_yy = re.compile(r'^\s*\d{1,2}\/\d{1,2}\/\d{2}\s*$')
    us_dt_dash_yy = re.compile(r'^\s*\d{1,2}\/\d{1,2}\/\d{2}\s*$')

    desired_dt_format = '%d/%m/%Y'

    patterns = {
            '%Y/%m/%d': iso_dt_slash,
            '%Y-%m-%d': iso_dt_dash,
            '%m/%d/%Y': us_dt_slash,
            '%m-%d-%Y': us_dt_dash,
            '%m-%d-%y': us_dt_slash_yy,
            '%m/%d/%y': us_dt_dash_yy,
            '%Y%m%d': iso_dt_basic
            }
    for dt_format, pattern in patterns.items():
        try:
            if re.match(pattern, input):                
                return "CONVERTED", datetime.strptime(input, dt_format).strftime(desired_dt_format)
        except Exception as e:
            return "EXCEPTION", datetime.now().replace(microsecond=0, second=0, minute=0, hour=0)
        return "NOT CONVERTED", datetime.now().replace(microsecond=0, second=0, minute=0, hour=0)
'''
    
    #dt = datetime.strptime('2022/12/21', '%Y/%m/%d').strftime(desired_dt_format)
    #print(dt)
if __name__ == '__main__':
    main()