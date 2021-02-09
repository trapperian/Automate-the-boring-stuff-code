# sandwich maker, asks user for bread type, protein, cheese, sauces and numbeer of sandwhiches total with costs attached
import pyinputplus as pyip
breadPrices = {"wheat": 2.50, "white": 2, "sourdough": 3, "rye": 3}
proteinPrices = {}
cheesePrices = {}
condimentPrices = {}


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



