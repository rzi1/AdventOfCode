import copy
def main():
    f = open("d2Input.txt", "r")
    content = f.readlines()
    array = content[0].split(",")
    for i in range(0, len(array)):
        array[i] = int(array[i])

    for x in range(100):
        for y in range(100):
            array2 = copy.deepcopy(array)
            array2[1] = x
            array2[2] = y
            array2 = opcode(array2)
            if array2[0] == 19690720:
                print((array2[1] * 100) + array2[2])



def opcode(code):
    length = len(code)
    n = 0
    while n < length:
        if code[i] == 1:
            code[code[i + 3]] = code[code[i + 1]] + code[code[i + 2]]
            increment = 4
        elif code[i] == 2:
            code[code[i + 3]] = code[code[i + 1]] * code[code[i + 2]]
            increment = 4
        elif code[i] == 3:
            code[i+1] = int(input("enter a number:"))
            increment = 2
        elif code[i] == 4:
            print(code[code[i+1]])
            increment = 2
        n += increment
    return code


main()
