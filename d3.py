import re
infile = '2024/inputs/d3.txt'
inputlines = [x for x in open(file=infile, mode='r').readlines()]


def part1():
    arr = []
    for i in inputlines:
        find_operands(input_arr=i, operands_array=arr)
    sum = 0
    for operand in arr:
        sum += int(operand[0]) * int(operand[1])
    print(sum)


def part2():
    do_list = []
    sum = 0
    for i in inputlines:
        get_do_list(input_arr=i, do_arr=do_list)
    arr = []
    for do in do_list:
        find_operands(do, arr)
    for operand in arr:
        sum += int(operand[0]) * int(operand[1])
    print(sum)


def get_do_list(input_arr, do_arr: list):
    dont_list = input_arr.split("don't()")
    length = len(dont_list)
    for i in range(length):
        if (i == 0):
            do_arr.append(dont_list[i])
        else:
            dont_split = dont_list[i].split("do()")
            dont_split_len = len(dont_split)
            if (dont_split_len > 1):
                for do in range(1, dont_split_len):
                    do_arr.append(dont_split[do])


def find_operands(input_arr, operands_array):
    regex = r"mul\(\d+,\d+\)"
    result = re.finditer(regex, input_arr)
    for match in result:
        op = match.group()
        operand_group = op.split("(")[1].replace(")", "")
        operands_array.append(operand_group.split(","))


print("--P1--")
part1()
print("--P2--")
part2()
