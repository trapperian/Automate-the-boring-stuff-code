#can one graph the number of times collatz has to run for numbers and see a pattern?
def collatz(number):
    if number == 1:
        pass
    elif number % 2 == 0:
        new_num = number // 2
        print(new_num)
        collatz(new_num)
    elif number % 2 != 0:
        new_num = 3 * number + 1
        print(new_num)
        collatz(new_num)


print("Enter an integer")
num = input()
try:
    collatz(int(num))
except ValueError:
    print("You must enter an integer.")
