import pyinputplus as pyip

while True:
    prompt = "Want to know how to keep an idiot busy for hours?\n"
    response = pyip.inputYesNo(prompt)

    if response == "no":
        print("Thank you. Have a nice day")
        break
    elif response == "yes":
        prompt = "Want to know how to keep an idiot busy for hours?\n"
        response = pyip.inputYesNo(prompt)
    else:
        print("{} is not a valid response.".format(response))
