import math


def add_fuel(weight):
    fuel = math.floor(int(weight)/3) - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + add_fuel(fuel)


def main():
    f = open("d1Input.txt", "r")
    contents = f.readlines()
    total = 0
    for x in contents:
        total += add_fuel(x)
    f.close()
    print(total)


main()
