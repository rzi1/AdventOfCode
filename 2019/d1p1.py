import math


def addfuel(weight):
    fuel = math.floor(int(weight)/3) - 2
    return fuel


def main():


    f = open("d1Input.txt", "r")
    contents = f.readlines()
    total = 0
    for x in contents:
        total += addfuel(x)
    f.close()
    print(total)


main()

