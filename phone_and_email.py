#! python 3
# Phone Number and Email Address Extractor
# Finds phone numbers and email address on the clipboard
import pyperclip, re

def main():
    # phone number regex
    phone_regex = re.compile(r'''(
        (\+\d{2})?                      # country code
        (\d{1,2}|\(\d{1,2}\))?          # area code
        (\s|-|\.)?                      # seperator
        (\d{4})                         # first 3 digits
        (\s|-|\.)                       # seperator
        (\d{4})                         # last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension, between two and five digits
        )''', re.VERBOSE)

    # email address regex, this regex won't match all possible email address, but will match any typical email address
    email_regex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+       # username
        @                       # @ symbol
        [a-zA-Z0-9.-]+          # domain name
        (\.[a-zA-Z]{2,4})       # dot-something, between two and four letters
        )''', re.VERBOSE)

    # find matches in clipboard text
    text = str(pyperclip.paste())
    matches = [] # empty list to store mataches
    
    for groups in phone_regex.findall((text)):
        phone_num = ' '.join([groups[1], groups[2], groups[4], groups[6], groups[7]]) # groups are country code, area code, first four digits, last four digits, and extension
        if groups[8] != '':
            phone_num += ' x' + groups[8]
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