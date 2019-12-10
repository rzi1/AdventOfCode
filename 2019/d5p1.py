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


def opcode(code):
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
            code[code[n + 1]] = int(input("enter a number:"))
            increment = 2
        elif opco == 4:
            print(find_pos(code[n+1], istr[1]))
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


array = [int(x) for x in open('d5Input.txt').read().split(',')]
opcode(array)
