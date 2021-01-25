#! python3
# multi-clipboard program via Automate the Boring Stuff by Al Sweigart, 2nd ed.

TEXT = {
    "agree": """That sounds great, I'll get back to you in full later.""",
    "busy": """Sorry, I do not have time at the moment, can we return to this next week?""",
    "upsell": """Would you consider making this a monthly donation?""",
}

import sys, pyperclip

if len(sys.argv) < 2:
    print("Usage: python mclip.py [keyphrase] - copy phrase text")
    sys.exit()
keyphrase = sys.argv[1]  # first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print("Text for " + keyphrase + " copied to clipboard.")
else:
    print("There is no text for " + keyphrase)
