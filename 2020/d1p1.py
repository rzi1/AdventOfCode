import itertools
inputs = [int(x) for x in open('Inputs/d1').readlines()]
combine = itertools.combinations(inputs, 2)
for i in combine:
    if i[0] + i[1] == 2020:
        print(i[0] * i[1])
