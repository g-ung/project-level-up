#! python3
# bullet_point_adder.py -- adds Wikipedia bullet points to the start
# of each line of text on the clipboard
import pyperclip

text = pyperclip.paste() # variable to store list of text

# Seperating list of text into lines and add asterix
lines = text.split("\n") # use split() to seperate the text at '\n', newlines, to get the list in one line of text
for i in range(len(lines)): # iterate thruough all indext in the 'lines' list
    lines[i] = '* ' + lines[i] # for each line in the list add '*' to start of the text

# join the modifed lines
text = '\n'.join(lines) # use join() to join the line  at '\n'

pyperclip.copy(text)
