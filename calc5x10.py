def calc_5x10(num):
    return num * 100000000 + (num**2 - num) * 500000
    ## [X * 1e8 + (X^2 - X) * 5e5]

def main():
    total =  (calc_5x10(46000) - calc_5x10(0))
    print(format(total, ","))


main()