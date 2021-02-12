#! python3
# mcb.pyw - saves and loads pieces of text to the clipboard.
# usage: py.exe mcb.pyw save <keyword> - saves clipboard to keyboard
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#        py.exe mcb.pyw lsit - loads all keywords to clipboard.

import shelve
import pyperclip as pyip
import sys

mcbShelf = shelve.open('mcb')








mcbShelf.close()
