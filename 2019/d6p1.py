
testcase = ["COM)B","B)C","C)D","D)E","E)F","B)G","G)H","D)I","E)J","J)K","K)L"]
edges = [str(x).strip() for x in open('d6Input.txt').readlines()]
orbits = dict()
for i in range(len(edges)):
    edge = edges[i].split(')')
    orbits[edge[1]] = edge[0]


def countOrbitsRecursive(orbits, node, count):
    if node == 'COM':
        return count
    count += 1
    return countOrbitsRecursive(orbits, orbits.get(node), count)


def countOrbits(orbits, node):
    return countOrbitsRecursive(orbits, node, 0)


def orbits_list(orbits, value):
    orbits_list = []
    while orbits.get(value) is not None:
        value = orbits.get(value)
        orbits_list.append(value)
    return orbits_list






orbit_count = 0
for i in orbits:
    orbit_count += countOrbits(orbits, i)

you = orbits_list(orbits, "YOU")
san = orbits_list(orbits, "SAN")

you_c = len(you) - 1
san_c =  len(san) - 1

while you[you_c] == san[san_c]:
    you_c -= 1
    san_c -= 1


print(san_c + you_c + 2)

print(orbit_count)



