#! python 3
'''
Phone Number and Email Address Extractor
Finds phone numbers and email address on the clipboard
Uses pyperclip package not part of standard Python library
Install with (Liniux\macOS) terminal command: pip3 install pyperclip

How to Use this Script
1. Select the text, Linux\macOS: COMMAND-A (Win: CTRL-A) 
2. Copy the text, Linux\macOS: COMMAND-C (Win: CTRL-C)
3. Run the script phone_and_email.py
'''
import pyperclip, re

def main():
    # phone number regex
    phone_regex = re.compile(r'''(
        (\W\d{2})?                      # country code, optional
        (\s|-|\.)?                      # separator
        (\d{1,2}|\(\d{1,2}\))?          # area code, eg. 03 or (03), optional
        (\s|-|\.)?                      # separator
        (\d{4})                         # first 4 digits
        (\s|-|\.)                       # seperator
        (\d{4})                         # last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension, between two and five digits, optional
        )''', re.VERBOSE)

    # email address regex, this regex won't match all possible email address, but will match any typical email address
    email_regex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+       # username
        @                       # @ symbol
        [a-zA-Z0-9.-]+          # domain name
        (\.[a-zA-Z]{2,4})       # dot-something, between two and four letters
        )''', re.VERBOSE)

    # use pyperclip() to find matches copied to clipboard text
    text = str(pyperclip.paste())
    matches = [] # empty list to store mataches
    
    for groups in phone_regex.findall((text)): # use findall() to return a phone numbers and email address in a list of tuples; one tuple for each match
        phone_num = ' '.join([groups[1], groups[3], groups[5], groups[7], groups[8]]) # groups are country code, area code, first four digits, last four digits
        if groups[9] != '':
            phone_num += ' x' + groups[9]
        matches.append(groups[0])
    for groups in email_regex.findall(text):
        matches.append(groups[0])

    # copy the results to the clipboard
    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print("Copied to clipboard: ")
        print('\n'.join(matches))
    else:
        print("No phone numbers or email address found.")

if __name__ == '__main__':
    main()
