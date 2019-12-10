def main():
    count = 0
    for i in range(402328, 864248):
        if check_grouping(i):
            if is_inc(i):
                count += 1
    print(count)


def check_grouping(num):
    num = str(num)
    for i in range(len(num) - 1):
        if num[i] == num[i+1]:
            if num.count(num[i]) == 2:
                return True


def is_inc(num):
    prev = 10
    while num:
        rem = int(num) % 10
        num = int(num)/10
        if rem > prev:
            return False
        prev = rem
    return True


main()
