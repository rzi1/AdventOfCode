relative = 0
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
    elif mode == 2:
        return array[relative + parm]

def find_literal(parm, mode):
    if mode == 0 or mode == 1:
        return parm
    elif mode == 2:
        return relative + parm


def opcode(code, input):
    global relative
    n = 0
    while n < len(code):
        istr = decoder(code[n])
        opco = istr[0]
        if opco == 1:
            code[find_literal(code[n + 3], istr[3])] = find_pos(code[n+1], istr[1]) + find_pos(code[n+2], istr[2])
            increment = 4
        elif opco == 2:
            code[find_literal(code[n + 3], istr[3])] = find_pos(code[n+1], istr[1]) * find_pos(code[n+2], istr[2])
            increment = 4
        elif opco == 3:
            code[find_literal(code[n + 1], istr[1])] = input
            increment = 2
        elif opco == 4:
            print(find_pos(code[n+1], istr[1]))
            increment = 2
        elif opco == 5: ## jump if true
            if find_pos(code[n+1], istr[1]) != 0:
                n = find_pos(code[n+2], istr[2])
                continue
            increment = 3
        elif opco == 6: #jump if false
            if find_pos(code[n+1], istr[1]) == 0:
                n = find_pos(code[n+2], istr[2])
                continue
            increment = 3
        elif opco == 7: ##less tahn
            if find_pos(code[n+1], istr[1]) < find_pos(code[n+2], istr[2]):
                code[find_literal(code[n + 3], istr[3])] = 1
            else:
                code[find_literal(code[n + 3], istr[3])] = 0
            increment = 4
        elif opco == 8: ## EQUAL
            if find_pos(code[n + 1], istr[1]) == find_pos(code[n+2], istr[2]):
                code[find_literal(code[n + 3], istr[3])] = 1
            else:
                code[find_literal(code[n + 3], istr[3])] = 0
            increment = 4
        elif opco == 9:
            relative += find_pos(code[n+1], istr[1])
            increment = 2
        elif opco == 99:
            return code
        n += increment


array = [int(x) for x in open('d9Input.txt').read().split(',')]
# array =[109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
for i in range(100000):
    array.append(0)
opcode(array, 2)