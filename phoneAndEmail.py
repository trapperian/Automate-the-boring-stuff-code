#! python3
# phoneAndEmail.py - finds phone numbers and email addresses on the clipboard.

import pyperclip
import re

phoneRegex = re.compile(
    r"""(
(\d{3}|\(\d{3}\))?              #area code check
(\s|-|\.)?                      #seperator
(\d{3})                         #first three digits
(\s|-|\.)                       #seperator
(\d{4})                         #last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?  #extension
)""",
    re.VERBOSE,
)

#TODO: create email regex.

#TODO: find matches in clipboard text.

#TODO: copy results to clibpard
