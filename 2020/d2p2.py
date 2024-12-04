p_array = [str(x).strip() for x in open("Inputs/d2").readlines()]
params = []
passwords = []
valid = 0
for i in p_array:
    i = i.split(':')
    t_params = i[0].split(' ')
    params.append(t_params)
    passwords.append(i[1].strip())
for i in range(len(passwords)):
    pos1, pos2 = params[i][0].split('-')
    p_char1, p_char2 = passwords[i][int(pos1) - 1], passwords[i][int(pos2) - 1]
    t_char = params[i][1]
    if (p_char1 == t_char) ^ (p_char2 == t_char):
        valid += 1

print(valid)
