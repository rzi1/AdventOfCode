import math
def find_slope_intercept(x1, x2, y1, y2):
    if x2 - x1 != 0:
        slope = (y2 - y1) / (x2 - x1)
        intercept = y1 - slope * x1
    else:
        slope = "undefined"
        intercept = x1
    if x1 > x2:
        if y1 > y2:
            dir = 0
        else:
            dir =1
    else:
        if y1 > y2:
            dir = 2
        else:
            dir = 3
    return str(slope) + "," + str(intercept) + "," + str(dir)


def calc_distance(x1, x2, y1, y2):
    return math.sqrt(math.pow((y2 - y1), 2) + math.pow((x2 - x1), 2))


def destroy(asteroids, best):
    x = int(best.split(",")[0])
    y = int(best.split(",")[1])
    slope_intercepts2 = []
    for k in asteroids:
        if k != best:
            x2 = int(k.split(',')[0])
            y2 = int(k.split(',')[1])
            slope_intercept = find_slope_intercept(x, x2, y, y2)
            slope_intercepts2.append(str(slope_intercept) + "," + str(k) + "," + str(calc_distance(x, x2, y, y2)))
    print(slope_intercepts2)
    # 0 = slope 1 = intercept 2 = dir 3 = x 4 = y 5 = distance

file = 'testinputd10.txt'
file2 = 'd10Input.txt'
lines = [str(x).strip() for x in open(file).readlines()]
count = 0
height = len(lines)
width = len(lines[0])
asteroids = []
for i in range(height):
    for j in range(width):
        if lines[i][j] == '#':
            asteroids.append(str(j) + "," + str(i))


max = 0
best = ""
for i in asteroids:
    x = int(i.split(',')[0])
    y = int(i.split(',')[1])
    slope_intercepts = []
    for j in asteroids:
        x2 = int(j.split(',')[0])
        y2 = int(j.split(',')[1])
        if j != i:
            slope_intercept = find_slope_intercept(x, x2, y, y2)
            if slope_intercepts.count(slope_intercept) == 0:
                slope_intercepts.append(slope_intercept)
        current = str(x) + "," + str(y)
    if max < len(slope_intercepts):
        max = len(slope_intercepts)
        best = current

print(best)
print(max)


destroy(asteroids, best)
