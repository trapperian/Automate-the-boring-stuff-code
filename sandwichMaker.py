# sandwich maker, asks user for bread type, protein, cheese, sauces and numbeer of sandwhiches total with costs attached
import pyinputplus as pyip
breadPrices = {"wheat": 2.50, "white": 2, "sourdough": 3, "rye": 3}
proteinPrices = {"chicken": 3, "turkey": 3.25, "ham": 2.50, "tofu": 1.50, "corned beef": 3.50}
cheesePrices = {"cheddar": 0.50, "swiss": 0.75, "provolone": 0.50, "mozzarella": 0.25, None: 0}
condimentPrices = {"mayo": 0.50, "mustard": 0.50, "1000 Island Dressing & Sauerkraut": 1.00, "tomato": 0.50, "onion": 0.75, "lettuce": 0.25}


print("Hello! Welcome to Sandy's Shell & Sandwich Shack on the Seashore!")
while True:
    numSandwiches = pyip.inputInt("How many sandwiches are we making today? ", min=1)
    breadType = pyip.inputMenu(["wheat", "white", "sourdough", "rye"], "What kind of bread would you like for your sandwich?\n")
    protein = pyip.inputMenu(["chicken", "turkey", "ham", "tofu", "corned beef"], "Good choice! What kind of meat are we having on your sandwich?\n")
    cheeseYN = pyip.inputYesNo("Would you like any cheese on this?")
    if cheeseYN == "yes":
        cheeseType = pyip.inputMenu(["cheddar", "swiss", "provolone", "mozzarella"], "What kind of cheese would you like?\n")
    else:
        cheeseType = None
    condiments = pyip.inputMenu(["mayo", "mustard", "1000 Island Dressing & Sauerkraut", "tomato", "onion", "lettuce"], "Alright, what other toppin's would you like?\n")



