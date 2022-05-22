# English to Pig Latin
print("enter the English message to translate into Pig Latin:") # prompt user to enter English text to translate into Pig Latin
message = input()

vowels = ('a', 'e', 'i', 'o', 'u', 'y') # tuple list to to stor all vowel + letter 'y'
pig_latin = [] # a list of the words in Pig Latin

for word in message.split():
    '''
    Iterate through message, use split() to get the list of words as separate stirngs.
    Then remove any non-letters from the start and end of each word, e.g. 'old'
    translates to 'oldyay' instead of 'old.yay'.  Save these non-letters to variable
    prefix_non_letters

    '''
    prefix_non_letters = ''
    while len(word) > 0 and not word[0].isalpha():
        '''
        use isalpha() in loop to determin if we should remove character from a word
        anc concatenate it to end of prefix_non_letters
        '''
        # separate the non-letters at the start of the this word
        prefix_non_letters += word[0]
        word = word[1:]
    
    if len(word) == 0:
        pig_latin.append(prefix_non_letters)
        continue

    # separate the non-letters at the end of the word
    suffix_non_letters= ''
    
    while not word[-1].isalpha():
        suffix_non_letters += word[-1]
        word = word[:-1]

    # remember if the word wasin uppercase or title case
    was_upper = word.isupper()
    was_title = word.istitle()
    word = word.lower() # make the word lowercase for translation

    # separate the consonants at the start of this word
    prefix_consonants = ''
    
    while len(word) > 0 and not word[0] in vowels:  # Loop through and remove consonants and store them in variable prefix_consonants.
    
        prefix_consonants += word[0]
        word = word[1:]
    # add the Pig Latin ending to the word
    if prefix_consonants != '':
        word += prefix_consonants + 'ay'
    else:
        word += 'yay'
        
    # set the word back to uppercase or title case
    if was_upper:
        word = word.upper()
    if was_title:
        word = word.title()

    # add the non-letters back to the start or end of the word
    pig_latin.append(prefix_non_letters + word + suffix_non_letters)

# join all the words back together into a single striing
print(' '.join(pig_latin))
        
