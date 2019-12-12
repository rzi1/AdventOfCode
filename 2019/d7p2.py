from intComputer import IntcodeComputer
from itertools import permutations, cycle
originalarray = [int(x) for x in open('Inputs/d7Input.txt').read().split(',')]
names = 'ABCDE'
max_signal = 0
phases = [5,6,7,8,9]
phaseperms = list(permutations(phases))
for phases in phaseperms:
    amplifiers = {}
    signal = 0
    for i in range(len(names)):
        amplifier = IntcodeComputer(originalarray, names[i])

        amplifier.send(phases[i])

        amplifiers[names[i]] = amplifier
    for j in cycle(names):
        amplifiers[j].send(signal)

        signal = amplifiers[j].receive()
        if signal is None:
            break
        if signal > max_signal:
            max_signal = signal

print(max_signal)