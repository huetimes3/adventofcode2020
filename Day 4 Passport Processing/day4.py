import re

def process_file(p_list):
    p = open('input.txt', 'r', encoding='utf-8')
    temp = {}
    for line in p:
        if len(line) == 1:
            p_list.append(temp)
            temp = {}
            continue
        line = line.split()
        for kvp in line:
            kvp = kvp.split(':')
            temp[kvp[0]] = kvp[1]
    p.close()
    
    
    
def validate_p():
    valid_p = 0
    p_list = []
    process_file(p_list)
    print(p_list)
    for p in p_list:
        try:
            if (1920 <= int(p['byr']) <= 2002) and (2010 <= int(p['iyr']) <= 2020) and\
               (2020 <= int(p['eyr']) <= 2030) and validate_hgt(p['hgt']) and validate_hcl(p['hcl']) and\
               validate_ecl(p['ecl']) and validate_pid(p['pid']):
                valid_p += 1
        except KeyError:
            continue
    return valid_p



def validate_hgt(hgt):
    if hgt[-2:] == 'cm':
        if 150 <= int(hgt[:-2]) <= 193:
            return True
    if hgt[-2:] == 'in':
        if 59 <= int(hgt[:-2]) <= 76:
            return True
    return False
      
      
      
def validate_hcl(hcl):
    hcl_re = re.compile(r'^#[0123456789abcdef]{6}$')
    hcl_mo = hcl_re.search(hcl)
    return not hcl_mo is None



def validate_ecl(ecl):
    valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return ecl in valid_ecl



def validate_pid(pid):
    pid_re = re.compile(r'^\d{9}$')
    pid_mo = pid_re.search(pid)
    return not pid_mo is None