# English to Pig Latin

print("Enter the English message to translate into Pig Latin:")
message = input()

VOWELS = ("a", "e", "i", "o", "u", "y")

pigLatin = []  # A list of words in Pig Latin.

for word in message.split():
    # separate the non-letters at the start of this word:
    prefixNonLetters = ""
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue
    # Separate the non-leters at the end of the word:
    suffixNonLetters = ""
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]
    # remember whether word was upper or title case
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower()  # making word lower case for translation

    # separate consants at start of word
    prefixConsonants = ""
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]
    # add Pig Latin ending to word:
    if prefixConsonants != "":
        word += prefixConsonants + "ay"
    else:
        word += "yay"
    # set word back to appropriate case
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()
    # bringing the non-letters back to start or end of word
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)
# Join all words back together into string_to_bytes
print(" ".join(pigLatin))
