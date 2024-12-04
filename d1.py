infile = '2024/inputs/d1.txt'
input = [x for x in open(file=infile, mode='r').readlines()]


def part1(arr1, arr2, length):

    sum = 0
    for j in range(length):
        sum += abs(arr1[j] - arr2[j])
    print(sum)


def part2(arr1, arr2, length):
    histogram = {}
    sum = 0
    for j in arr2:
        if (j in histogram.keys()):
            histogram[j] += 1
        else:
            histogram[j] = 1
    for k in arr1:
        if (k in histogram.keys()):
            sum += k * histogram[k]
    # for i in range(length):

    print(sum)


arr1 = []
arr2 = []
for i in input:
    split = i.split()
    arr1.append(int(split[0]))
    arr2.append(int(split[1]))
arr1.sort()
arr2.sort()
length = len(arr1)
print("--P1--")
part1(arr1=arr1, arr2=arr2, length=length)
print("--P2--")
part2(arr1=arr1, arr2=arr2, length=length)
