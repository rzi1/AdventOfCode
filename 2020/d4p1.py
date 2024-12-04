import re
passports = [str(x).replace("\n",  " ") for x in open("Inputs/d4").read().split("\n\n")]
passport_dictlist = [dict() for i in range(len(passports))]
for i in range(len(passports)):
    passport = passports[i].split(" ")
    for field in passport:
        field = field.split(":")
        passport_dictlist[i][field[0]] = field[1]
hcl_validate = re.compile('^#{1}[0-9a-f]{6}')
hgt_cm = re.compile('[0-9]*cm')
hgt_in = re.compile('[0-9]*in')
valid_passports = 0
for passport_dict in passport_dictlist:
    if 'byr' not in passport_dict:
        continue
    else:
        byr = int(passport_dict['byr'])
        if byr > 2002 or byr < 1920:
            continue
    if 'iyr' not in passport_dict:
        continue
    else:
        iyr = int(passport_dict['iyr'])
        if iyr < 2010 or iyr > 2020:
            continue
    if 'eyr' not in passport_dict:
        continue
    else:
        eyr = int(passport_dict['eyr'])
        if eyr < 2020 or eyr > 2030:
            continue
    if 'hgt' not in passport_dict:
        continue
    else:
        hgt = passport_dict['hgt']
        if not(hgt_cm.match(hgt) or hgt_in.match(hgt)):
            continue
        else:
            hgt_num = int(re.sub('[a-z]', '', hgt))
            if hgt_cm.match(hgt):
                if hgt_num < 150 or hgt_num > 193:
                    continue
            if hgt_in.match(hgt):
                if hgt_num < 59 or hgt_num > 76:
                    continue
    if 'hcl' not in passport_dict:
        continue
    else:
        hcl = passport_dict['hcl']
        if not (hcl_validate.match(hcl)):
            continue
    if 'ecl' not in passport_dict:
        continue
    else:
        ecl = passport_dict['ecl']
        if not (ecl == 'amb' or ecl == 'blu' or ecl == 'brn' or ecl == 'gry' or ecl == 'grn' or ecl == 'hzl' or ecl == 'oth'):
            continue
    if 'pid' not in passport_dict:
        continue
    else:
        if len(passport_dict['pid']) != 9:
            continue
    valid_passports += 1
print(valid_passports)