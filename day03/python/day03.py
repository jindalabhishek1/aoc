def count_trees_encountered(lst,right, down):
    rightMoves = right
    downMoves = down
    i = j = count = 0
    lenLst = len(lst)
    lenLstItem = len(lst[0])
    print (lenLst, lenLstItem)
    while (i < lenLst):
        print ("i: ", i)
        
        rightMoved = 0
        while True:
            j += 1
            rightMoved += 1
            if j == lenLstItem: j = j % lenLstItem
            if rightMoved == rightMoves: break
        i += downMoves
        if lst[i][j] == '#': count += 1
        print ("i: ", i, "j: ", j, "lst[i][j]: ", lst[i][j], "count: ", count)
        if i == lenLst - 1: break
        
    return count


fname = input("Enter file name: ")
if len(fname) < 1: fname = '../input.txt'

lst = list()
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    lst.append(line)

# print (lst)
result = list()
while True:
    try:
        inp = input("Enter Right moves or 'x' or 'X' to exit: ")
        if (inp == 'x' or inp == 'X'): break
        right = int(inp)
        inp = input("Enter Down moves or 'x' or 'X' to exit: ")
        if (inp == 'x' or inp == 'X'): break
        down = int(inp)
    except:
        print ("Enter valid input or type 'x' or 'X' to exit!!!")
        continue
    count = count_trees_encountered(lst, right, down)
    print(count)
    result.append((right, down, count))
product = 1
for item in result:
    product *= item[2]
print (product)