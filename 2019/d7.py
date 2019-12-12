import copy
from intComputer import IntcodeComputer
from itertools import permutations
originalarray = [int(x) for x in open('Inputs/d7Input.txt').read().split(',')]
phases = [0,1,2,3,4]
phaseperms = list(permutations(phases))
highstr = 0
for i in phaseperms:
    strength = 0
    for j in i:
        amp = IntcodeComputer(originalarray)
        amp.send(j)
        amp.send(strength)

        strength = amp.receive()

    if strength > highstr:
        highstr = strength

print(highstr)