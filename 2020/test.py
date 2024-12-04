from random import randint

test = "{:016d}".format(randint(0, 1e15))
print(test)
print(int(test))