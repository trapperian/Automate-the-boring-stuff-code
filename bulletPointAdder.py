#! python3
# bulletPointAdder.py - Adds wikipedia bullet points to the start of each line of text on clipboard

import pyperclip

text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split("\n")  # splitting lines on clipboard
for i in range(len(lines)):  # looping through each of the splitlines
    lines[i] = "* " + lines[i]  # adding star and space to each line
text = "\n".join(lines)  # turning lines into one string for copy function
pyperclcip.copy(text)
