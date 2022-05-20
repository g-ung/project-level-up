#! python3
# myclippy -- a multi-clipboard program

# dictionary to store you predefined message phrases
import sys
import pyperclip

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""", 'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

# handle command line arguments
if len(sys.argv) < 2 :
    print("Usage: python mclip.py [keyphrase] - copy phrase text")
    sys.exit()

keyphrase = sys.argv[1] # first command line arg is the keyphrase, i.e. the key in TEXT dict., stored in the variable keyphrase

# copy the right phrase
if keyphrase in TEXT: # checks if the keyphrase exist in TEXT dict.
    pyperclip.copy(TEXT[keyphrase])
    '''
    If the key phrase exist the corresponding value to that key is copied to the clipboard,
    and printed to a message saying we copied the value
    '''
    print("Text for {} copied to clipboard".format(keyphrase))
else:
    print("There is no text for {}".format(keyphrase)) # if the key phrase does not exist print messaing saying no key phrase with that name