import copy
from itertools import permutations
def decoder(instruct):
    a = str(instruct)
    b = [int(a[-2:])]
    for d in a[-3::-1]:
        b.append(int(d))
    b.extend([0, 0, 0])
    return b


def find_pos(parm, mode):
    if mode == 0:
        return array[parm]
    elif mode == 1:
        return parm


def opcode(code, phase, strength):
    n = 0
    while n < len(code):
        istr = decoder(code[n])
        opco = istr[0]
        if opco == 1:
            code[code[n + 3]] = find_pos(code[n+1], istr[1]) + find_pos(code[n+2], istr[2])
            increment = 4
        elif opco == 2:
            code[code[n + 3]] = find_pos(code[n+1], istr[1]) * find_pos(code[n+2], istr[2])
            increment = 4
        elif opco == 3:
            if phase >= 0:
                code[code[n + 1]] = phase
                phase = -1
            else:
                code[code[n + 1]] = strength
            # code[code[n + 1]] = int(input("enter a number:"))
            increment = 2
        elif opco == 4:
            return find_pos(code[n+1], istr[1])
            increment = 2
        elif opco == 5: ## jump if true
            if find_pos(code[n+1],istr[1]) != 0:
                n = find_pos(code[n+2], istr[2])
                continue
            increment = 3
        elif opco == 6: #jump if false
            if find_pos(code[n+1],istr[1]) == 0:
                n = find_pos(code[n+2], istr[2])
                continue
            increment = 3
        elif opco == 7: ##less tahn
            if find_pos(code[n+1], istr[1]) < find_pos(code[n+2], istr[2]):
                code[code[n + 3]] = 1
            else:
                code[code[n+3]] = 0
            increment = 4
        elif opco == 8: ## EQUAL
            if find_pos(code[n+1], istr[1]) == find_pos(code[n+2], istr[2]):
                code[code[n + 3]] = 1
            else:
                code[code[n+3]] = 0
            increment = 4
        elif opco == 99:
            return code
        n += increment


originalarray = [int(x) for x in open('d7Input.txt').read().split(',')]
# opcode(array)

testarray = originalarray

phases = [0,1,2,3,4]
phaseperms = list(permutations(phases))
highstr = 0
for i in phaseperms:
    strength = 0
    for j in range(len(i)):
        array = copy.deepcopy(testarray)
        strength = opcode(array, i[j], strength)
    if strength > highstr:
        highstr = strength


print(highstr)
