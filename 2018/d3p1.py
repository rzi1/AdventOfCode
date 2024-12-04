

# cut

# claim #123 @ 3,2: 5x4 == left, top: Wide x Tall

# find overlaps size of field 1000
def get_input(item):
    fields = item.split('@')
    fields2 = fields[1].split(':')
    side_top = fields2[0].split(',')
    length_width = fields2[1].split('x')
    return side_top, length_width


# def find_area():
#
#
# def find_overlaps():




pos, area = get_input('#1 @ 1,3: 4x4')

print(pos)
print(area)