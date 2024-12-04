import math
def find_trees(x_speed, y_speed):
    tree_map = [str(x).strip() for x in open("Inputs/d3").readlines()]
    x_pos = 0
    y_pos = 0
    x_speed = x_speed
    y_speed = y_speed
    trees_hit = 0
    while y_pos < len(tree_map) - 1:
        x_pos += x_speed
        y_pos += y_speed
        if y_pos > len(tree_map) - 1:
            break
        if x_pos >= len(tree_map[y_pos]):
            tree_map[y_pos] += tree_map[y_pos] * math.ceil(x_pos/len(tree_map[y_pos]))
        if tree_map[y_pos][x_pos] == '#':
            trees_hit += 1
    return trees_hit
## p1
print(find_trees(3,1))
## p2
print(find_trees(1,1) * find_trees(3,1) * find_trees(5,1) * find_trees(7,1) * find_trees(1,2))
