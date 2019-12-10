import math


def main():
    f = open("d3Input.txt", "r")
    content = f.readlines()
    wire1 = content[0].split(",")
    wire2 = content[1].split(",")
    path1 = find_path(wire1)
    path2 = find_path(wire2)
    intersects = find_intersects(path1, path2)
    print("Least Steps: ", find_steps(intersects, path1, path2))


def find_steps(intersects, path1, path2):
    least_steps = None
    for item in intersects:
        steps = (path1.index(item) + 1) + (path2.index(item) + 1)
        if least_steps is None:
            least_steps = steps
        elif steps < least_steps:
            least_steps = steps
    return least_steps



def find_path(wire):
    path = []
    x = 0
    y = 0
    for i in wire:
        dis = int(i[1:])
        for j in range(dis):
            if i[0] == "R":
                x += 1
            elif i[0] == "L":
                x -= 1
            elif i[0] == "U":
                y += 1
            elif i[0] == "D":
                y -= 1
            path.append(str(x) + "," + str(y))
    return path


def find_intersects(path1, path2):
    intersects = set(path1).intersection(path2)
    return list(intersects)


def find_shortest(intersects):
    shortest = None
    for i in intersects:
        coords = i.split(",")
        distance = math.fabs(int(coords[0])) + math.fabs(int(coords[1]))
        if shortest is None:
            shortest = distance
        elif distance < shortest:
            shortest = distance
    return shortest


main()
