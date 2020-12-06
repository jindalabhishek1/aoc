import re

count = 0

fhand = open('../input.txt')
for line in fhand:
    line = line.rstrip()
    inp = line
    inp = inp.split()
    inp[0] = inp[0].split('-')
    inp[1] = inp[1][:1]
    # res = inp[2].count(inp[1])
    # if res >= int(inp[0][0]) and res <= int(inp[0][1]): count += 1
    print(inp)
    if inp[1] == inp[2][int(inp[0][0]) - 1] and inp[1] != inp[2][int(inp[0][1]) - 1]:
        count += 1
    elif inp[1] != inp[2][int(inp[0][0]) - 1] and inp[1] == inp[2][int(inp[0][1]) - 1]:
        count += 1
    print ("inp: ", inp, "count: ", count, "\n")

print (count)
