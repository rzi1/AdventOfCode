infile = '2024/inputs/d2.txt'
input = [x for x in open(file=infile, mode='r').readlines()]


def part1():
    safe = 0
    for k in input:
        split = k.split()
        if check_safe(split):
            safe += 1
    print(safe)


def part2():
    safe = 0
    for k in input:
        split = k.split()
        if check_safe(split):
            safe += 1
        else:
            length = len(split)
            for b in range(length):
                new_check = split.copy()
                new_check.pop(b)
                if check_safe(new_check):
                    safe += 1
                    break
    print(safe)


def check_safe(arr):
    length = len(arr)
    ascending = None
    for j in range(length - 1):
        diff = int(arr[j]) - int(arr[j+1])
        if (ascending is True and diff < 0) or abs(diff) > 3 or abs(diff) < 1 or (ascending is False and diff > 0):
            return False
        if diff > 0 and ascending is None:
            ascending = True
        if diff < 0 and ascending is None:
            ascending = False
    return True


print("--P1--")
part1()
print("--P2--")
part2()
