from intComputer import IntcodeComputer
code = [int(x) for x in open('Inputs/d9Input.txt').read().split(',')]
ic = IntcodeComputer(code)
ic.send(1)
print(ic.receieve())
