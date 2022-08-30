#! python 3
'''
Regex Version of strip() Method
Write a function that takes a string and does the same
thing as the strip() string method.

REQUIREMENTS
1. If no arguments are passed other than the string to strip,
then whitespace characters will be removed from leading and
trailing of the string
2. The characters specified in the second argument to the
funtion will be removed from the string
'''
import re

def strip_regex(text, strip_this=None):
    if strip_this is None:
        '''
        Use character classes to define regex conditions, i.e.
        '\s' and '.*' (greedy) to match everything.
        REFERENCE:
        https://automatetheboringstuff.com/2e/chapter7/
        https://python-tutorials.in/regex-greedy/

        Combine stripping the leading and trailing whitespace in one 
        regex
        '''
        strip_whitespace = re.compile(r'^\s*|\s*$') # strip any space, tab, or newline
        text = strip_whitespace.sub('', text) # replace whitespace wtih empty string in string, text
        return text
    else:
        '''
        Use re.escape(pattern) funtion to strip any characters or 
        escape characters to your text
        REFERENCE:
        https://docs.python.org/3/library/re.html
        '''
        strip_it = re.compile(re.escape(strip_this)) # strip whatever arg strip_this is assigned to
        text = re.sub(strip_it, '', text)
        return text
    
def main():
    # test regex version of strip() method
    print('Regex version of strip() method.  BEGIN TEST...\n')

    print('TEST 1: Whitespaces')
    print(strip_regex('     Strip this string with whitespaces      '))
    print()
    print('TEST 2: Hyphens')
    print(strip_regex('-----Strip this string with hyphens-----\n', '-'))
    print('TEST 3: ox')
    print(strip_regex('oxStrip this string with OXsox\n', 'ox'))
    print('TEST 4: Hashes')
    print(strip_regex('#####Strip this string with hashes#####\n', '#'))
    print('TEST 5: Asterix')
    print(strip_regex('*****Strip this string with asterix*****\n', '*'))
    print('TEST 6: Comma')
    print(strip_regex('Strip, these, commas\n', ','))
    print('TEST 7: Leading spaces')
    print(strip_regex('     Strip leading spaces'))
    print('END TEST...')

if __name__ == '__main__':
    main()