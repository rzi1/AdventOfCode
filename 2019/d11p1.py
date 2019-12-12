from intComputer import IntcodeComputer

code = [int(x) for x in open('Inputs/d11Input.txt').read().split(',')]
robot = IntcodeComputer(code)
directions = ["up", "down", "left", "right"]
direction = directions[0]
robot.send(0)
    