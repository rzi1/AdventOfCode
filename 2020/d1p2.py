import itertools
inputs = [int(x) for x in open('Inputs/d1').readlines()]
combine = itertools.combinations(inputs, 3)
for i in combine:
    if i[0] + i[1] + i[2] == 2020:
        print(i[0] * i[1] * i[2])
