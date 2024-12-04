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
    min, max = params[i][0].split('-')
    num_char = passwords[i].count(params[i][1])
    if num_char >= int(min) and num_char <= int(max):
        valid += 1

print(valid)
