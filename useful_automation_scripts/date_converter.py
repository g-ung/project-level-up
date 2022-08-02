#! python 3
'''
Convert ISO 8601 and US Date Format to DD-MM-YYYY

Use regular expressions to find date that are in 
ISO 8601/US date pattern, then converts them to 
DD/MM/YYYY or DD/MM/YY format.
'''

import re
from datetime import datetime

def main():
    # date regex
    iso_dt_slash = re.compile(r'^\s*\d{4}\/\d{1,2}\/\d{1,2}\s*$')
    iso_dt_dash = re.compile(r'^\s*\d{4}-\d{1,2}-\d{1,2}\s*$')
    iso_dt_basic = re.compile(r'^\s*\d{4}\d{1,2}\d{1,2}\s*$')
    us_dt_slash = re.compile(r'^\s*\d{1,2}\/\d{1,2}\/\d{4}\s*$')
    us_dt_dash = re.compile(r'^\s*\d{1,2}-\d{1,2}-\d{4}\s*$')
    us_dt_slash_yy = re.compile(r'^\s*\d{1,2}\/\d{1,2}\/\d{2}\s*$')
    us_dt_dash_yy = re.compile(r'^\s*\d{1,2}-\d{1,2}-\d{2}\s*$')

    desired_dt_format = '%d/%m/%Y'
    '''
    patterns = {
            '%Y/%m/%d': iso_dt_slash,
            '%Y-%m-%d': iso_dt_dash,
            '%m/%d/%Y': us_dt_slash,
            '%m-%d-%Y': us_dt_dash,
            '%m-%d-%y': us_dt_slash_yy,
            '%m/%d/%y': us_dt_dash_yy,
            '%Y%m%d': iso_dt_basic
            }
    '''
    # date match and write to output file
    input_file = "/Users/gabe_ung/Desktop/dates.txt"
    output_file = "/Users/gabe_ung/Desktop/converted_dates.txt"
    with open(input_file, 'r') as in_f, open(output_file, 'w') as out_f:
        for line in in_f.readlines():
            line = line.strip()
            if re.match(iso_dt_slash, line):
                dt_obj = datetime.strptime(line, '%Y/%m/%d')
            elif re.match(iso_dt_dash, line):
                dt_obj = datetime.strptime(line, '%Y-%m-%d')
            elif re.match(us_dt_slash, line):
                dt_obj = datetime.strptime(line, '%m/%d/%Y')
            elif re.match(us_dt_dash, line):
                dt_obj = datetime.strptime(line, '%m-%d-%Y')
            elif re.match(us_dt_slash_yy,line):
                dt_obj = datetime.strptime(line, '%m/%d/%y')
            elif re.match(us_dt_dash_yy, line):
                dt_obj = datetime.strptime(line, '%m-%d-%y')
            elif re.match(iso_dt_basic, line):
                dt_obj = datetime.strptime(line, '%Y%m%d')
            out_f.write(dt_obj.strftime(desired_dt_format) + '\n')

if __name__ == '__main__':
    main()