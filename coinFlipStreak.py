import random

flip_list = []
numberOfStreaks = 0
streak = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    for i in range(100):
        flip_list.append(random.randint(0, 1))
    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(len(flip_list)):
        if i == 0:
            pass
        elif (
            flip_list[i] == flip_list[i - 1]
        ):  # checks if current list item is the same as before
            streak += 1
        else:
            streak = 0
        if streak == 6:
            numberOfStreaks += 1
    flip_list = []
print("Chance of streak: %s%%" % (numberOfStreaks / (100)))
