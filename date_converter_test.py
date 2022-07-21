import re
from datetime import datetime

with open("/Users/gabe_ung/Desktop/testdate.txt", "r") as fi, open("out.txt","w") as fo:
    for line in fi:
        line = line.strip()
        dateObj = None
        if re.match(r"^\d{8}$", line):
            dateObj = datetime.strptime(line,'%Y%m%d')
        elif re.match(r"^\d{1,2}/", line):
            dateObj = datetime.strptime(line,'%m/%d/%Y')
        elif re.match(r"^[a-z]{3}", line, re.IGNORECASE):
            dateObj = datetime.strptime(line,'%b %d %Y')
        elif re.match(r"^\d{1,2} [a-z]{3}", line, re.IGNORECASE):
            dateObj = datetime.strptime(line,'%d %b %Y')
        fo.write(dateObj.strftime('%m-%d-%Y') + "\n")