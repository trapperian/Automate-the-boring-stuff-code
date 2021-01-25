#! python3
#bulletPointAdder.py - Adds wikipedia bullet points to the start of each line of text on clipboard

import pyperclip
text = pyperclip.paste()

#TODO: separate lines and add stars.

# Separate lines and add stars.
lines = text.split('\n')   #splitting lines on clipboard
for i in range(len(lines)):  #looping through each of the splitlines
    lines[i] = '* ' + lines[i] #adding star and space to each line

pyperclcip.copy(text)
