k = 10

array = [106,111,117,43,158,21,182,27,112,126,144,138,21,47,111,140,73,131,140,159,147,191,152,196,135,83,143,146,121,166,161,91,122,63,111,186,24,116,115,57,5,71,66,79,115,177,37]

def bob(num):
    solutions = []
    for i in reversed(range(1, num + 1)):
        solution = []
        remaining = num
        for j in range(1, num):
            print(i*j)
            if(i * j <= remaining):
                solution.append([j]*i)
                remaining -= i*j
            if(remaining == 0):
                solutions.append(solution)
        print(solutions)


# bob(5)
sum = 0
for i in range(23,100):
    print(i)
    sum += i
print(sum)