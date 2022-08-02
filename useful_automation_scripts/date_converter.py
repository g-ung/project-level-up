#! python 3
'''
Convert ISO 8601 and US Date Format to DD-MM-YYYY

Use regular expressions to find date that are in 
ISO 8601/US date pattern, then converts them to 
DD/MM/YYYY or DD/MM/YY format.
'''

import re
from datetime import datetime

def date_converter(input_date):
    # date regex
    iso_dt_slash = re.compile(r'^\s*\d{4}\/\d{1,2}\/\d{1,2}\s*$')
    iso_dt_dash = re.compile(r'^\s*\d{4}-\d{1,2}-\d{1,2}\s*$')
    iso_dt_basic = re.compile(r'^\s*\d{4}\d{1,2}\d{1,2}\s*$')
    us_dt_slash = re.compile(r'^\s*\d{1,2}\/\d{1,2}\/\d{4}\s*$')
    us_dt_dash = re.compile(r'^\s*\d{1,2}-\d{1,2}-\d{4}\s*$')
    us_dt_slash_yy = re.compile(r'^\s*\d{1,2}\/\d{1,2}\/\d{2}\s*$')
    us_dt_dash_yy = re.compile(r'^\s*\d{1,2}-\d{1,2}-\d{2}\s*$')

    desired_dt_format = '%d/%m/%Y'
    
    output_file = "converted_dates.txt"
    with open(output_file, 'w') as out_f:
        if re.match(iso_dt_slash, input_date):
            dt_obj = datetime.strptime(input_date, '%Y/%m/%d')
        elif re.match(iso_dt_dash, input_date):
            dt_obj = datetime.strptime(input_date, '%Y-%m-%d')
        elif re.match(us_dt_slash, input_date):
            dt_obj = datetime.strptime(input_date, '%m/%d/%Y')
        elif re.match(us_dt_dash, input_date):
            dt_obj = datetime.strptime(input_date, '%m-%d-%Y')
        elif re.match(us_dt_slash_yy,input_date):
            dt_obj = datetime.strptime(input_date, '%m/%d/%y')
        elif re.match(us_dt_dash_yy, input_date):
            dt_obj = datetime.strptime(input_date, '%m-%d-%y')
        elif re.match(iso_dt_basic, input_date):
            dt_obj = datetime.strptime(input_date, '%Y%m%d')
        out_f.write(dt_obj.strftime(desired_dt_format) + '\n')
        '''
            return 'CONVERTED', dt_obj.strftime(desired_dt_format)
        except Exception as e:
            return 'EXCEPTION', datetime.now().replace(microsecond=0, second=0, minute=0, hour=0)
        return 'NOT CONVERTED', datetime.now().replace(microsecond=0, second=0, minute=0, hour=0)
        '''
def main():
    # date match and write to output file
    input_file = "/Users/gabe_ung/Desktop/dates.txt"
    with open(input_file, 'r') as in_f: 
        for line in in_f.readlines():
            line = line.strip()
            date_converter(line)
            #print("Input Date: {}] [{}] to [{}]".format(line, status, date_obj))

if __name__ == '__main__':
    main()
