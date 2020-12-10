import re

def inp():    
    fname = input("Enter file name: ")
    if len(fname) < 1: fname = '../input.txt'

    lst = list()
    temp = None
    fhand = open(fname)

    # print (fhand.readlines())
    for line in fhand:
        if temp is None: temp = dict()
        line = line.rstrip()
        # print(line)
        if (len(line) < 1): 
            lst.append(temp)
            temp = None
            continue
        line = line.split()
        
        for i in line:
            
            i = i.split(":")
            temp[i[0]] = i[1]
    lst.append(temp)
    # print(lst)
    return lst

def regular_string(field):
    if field == "byr" : reg = '^(19[2-9]\d|200[0-2])$'
    elif field == "iyr" : reg = '^(20[1]\d|2020)$'
    elif field == "eyr" : reg = '^(20[2]\d|2030)$'
    elif field == "hgt" : reg = '(1[5-8]\d|19[0-3])(?=cm)|(59|6\d|7[0-6](?=in))'
    elif field == "hcl" : reg = '^#([0-9a-f]{6}$)'
    elif field == "ecl" : reg = '\\b(amb|blu|brn|gry|grn|hzl|oth)\\b'
    elif field == "pid" : reg = '(?<!.)\d{9}(?!.)'
    elif field == "cid" : reg = '(.*)'
    else : reg = None
    return reg

def check(temp):
    listOfKeys = list(temp.keys())
    listOfValues = list(temp.values())
    i = 0
    length = len(listOfKeys)
    if length < 7 : return False
    elif length < 8 and listOfKeys.count('cid') != 0 : return False
    else:
        while (i < length):
            reg = regular_string(listOfKeys[i])
            res = re.findall(reg, listOfValues[i])
            i += 1
            if len(res) == 0: return False
    return True

def count_valid_passports(lst):
    count = 0
    num = 0
    for item in lst:
        res = check(item)
        if res is True : count += 1
    return count

# start 

lst = inp()
count = count_valid_passports(lst)
print ("Total valid passports: ", count)