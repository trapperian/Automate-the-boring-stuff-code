spam = ["apples", "bananas", "tofu", "cats"]
check_empty = []
check_one = ["cats"]


def list_to_string(lst):
    new_string = ""
    if len(lst) == 0:  # empty list alternative
        print("Nothing to see here.")
    elif len(lst) == 1:  # if list is only one item list.
        print("Your list has only one item, it is: " + str(lst[0]))
    else:  # otherwise if items are in list
        for i in lst:
            if i != lst[-1]:
                new_string += i + ", "
            else:
                new_string += "and " + i
    return new_string


test1 = list_to_string(spam)
print(test1)
print(list_to_string(check_empty))
print(list_to_string(check_one))
