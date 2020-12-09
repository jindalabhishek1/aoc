def inp():    
    fname = input("Enter file name: ")
    if len(fname) < 1: fname = '../sample_input.txt'

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

def check(temp):
    listOfKeys = list(temp.keys())
    lenght = len(listOfKeys)
    if lenght == 8: return True
    if lenght == 7:
        if (listOfKeys.count('cid')) == 0 : return True
    return False

def count_valid_passports(lst):
    count = 0
    for item in lst:
        # print (type(item))
        res = check(item)
        if res is True : count += 1
        # print("item: ", item, "res: ", res, "count: ", count)
    return count

# start 

lst = inp()
# print(lst)
count = count_valid_passports(lst)
print ("Total valid passports: ", count)