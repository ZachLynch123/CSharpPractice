

def countdown(x):
    if x == 0:
        print("Done!")
        return
    else: 
        print(x, "...")
        countdown(x - 1)
        return

countdown(5)


## building factorial and power functions

def power(num, pwr):
    if pwr == 0:
        return 1
    else:
        return num * power(num, pwr - 1)


def factorial(num):
    if num == 0:
        return 1

    else:
        return num * factorial(num - 1)


print("{} to the power of {} is {}".format(5, 3, power(5, 3)))
print("{} to the power of {} is {}".format(5, 3, power(7, 5)))
print("{}! is {}".format(4, factorial(4)))
print("{}! is {}".format(2, factorial(2)))