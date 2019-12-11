import math
import operator
def calc_distance(a,b):
    x1,y1= a
    x2,y2 = b
    return math.hypot((y2-y1), (x2-x1))

def find_angle(a,b):
    return math.degrees(math.atan2(b[0] - a[0], a[1] - b[1]) % (2 * math.pi))


def destroy(asteroids, best):
    angle_distance = []
    angles = []
    for k in asteroids:
        if k != best:
            angle = find_angle(best, k)
            distance = calc_distance(best, k)
            angle_distance.append([angle, distance, k])
            if angles.count(angle) == 0:
                angles.append(angle)
    angle_distance = sorted(angle_distance, key=operator.itemgetter(0,1))
    angles.sort()
    count = 0
    for j in range(len(angles)):
        for i in range(len(angle_distance)):
            if angles[j] == angle_distance[i][0]:
                print(count, angle_distance[i][2])
                count += 1
                angle_distance.pop(i)


    print(angle_distance)
    print(angles)

def count(asteroids, asteroid):
    visible = []
    for i in asteroids:
        if i == asteroid:
            continue
        angle = find_angle(i, asteroid)
        if visible.count(angle) == 0:
            visible.append(angle)
    return len(visible)


def get_most(asteroids):
    most = 0
    for i in asteroids:
        curr_count = count(asteroids, i)
        if curr_count > most:
            most = curr_count
            best = i
    return best, most

def main():
    file = 'testinpitd10.txt'
    file2 = 'd10Input.txt'
    lines = [str(x).strip() for x in open(file).readlines()]
    height = len(lines)
    width = len(lines[0])
    asteroids = []
    for i in range(height):
        for j in range(width):
            if lines[i][j] == '#':
                asteroids.append((j, i))
    best, max = get_most(asteroids)
    asteroids.sort()
    print(best)
    print(max)
    destroy(asteroids, best)
    # test = (11,12)
    # print(find_angle(best, test))
    # print(calc_distance(best, test))

main()
