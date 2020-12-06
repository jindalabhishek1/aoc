# sample input [1721, 979, 366, 299, 675, 1456]

# sort function
def sort (lst):
    length = len(lst)
    mid = int(length/2)
    if length > 1:
        
        arr1 = lst[:mid]
        arr2 = lst[mid:]
    
        sort(arr1)
        sort(arr2)
    
    
        i = j = k = 0
        # print ("arr1[i]: ", arr1[i])
        # print ("arr2[j]: ", arr2[j])
        while (i < len(arr1) and j < len(arr2)):
            if arr1[i] < arr2[j]:
                lst[k] = arr1[i]
                i += 1
            else:
                lst[k] = arr2[j]
                j += 1
            k += 1
        while i < len(arr1):
            lst[k] = arr1[i]
            i += 1
            k += 1
            
        while j < len(arr2):
            lst[k] = arr2[j]
            j += 1
            k += 1
            
            
    #print ("lst: ", lst, " end\n")    
    
# binary searching
# Not using it in optimized code
def search(lst, numToFind):
    print ("****Search function****")
    mid = len(lst) // 2
    print ("lst: ", lst, "numToFind: ", numToFind, "lst[mid]: ", lst[mid])
    
    if len(lst) > 1:
        if numToFind < lst[mid]:
            result = search(lst[:mid],numToFind)
        else:
            result = search(lst[mid:], numToFind)
    else:
        if numToFind == lst[mid]:
            print ("Returning to caller")
            return lst[mid]
        else:
            return None
    return result
    
def find(lst, num):
    # print ("****find funtion****")
    # numToFind = num - lst[-1]
    # result = None
    # if len(lst) < 2:
    #     if lst[0] == numToFind:
    #         result = lst[0]
    # else:
    #     result = search(lst, numToFind)
    #     print ("lst: ", lst, "numToFind: ", numToFind, "result: ", result)
    #     if result == None: 
    #         lst = lst[:-1]
    #         result = find(lst, num)
    #     else:
    #         return [result,lst[-1]]
    # return result
    arr_size = len(lst)
    l = 0
    r = arr_size-1
     
    # traverse the array for the two elements
    while l<r:
        if (lst[l] + lst[r] == num):
            return [lst[l], lst[r]]
        elif (lst[l] + lst[r] < num):
            l += 1
        else:
            r -= 1
    return None
lst = list()
# print ("Input Numbers: ")
# while (True) :
#     temp = input()
#     if len(temp) < 1 : break
#     temp = int(temp)
#     lst.append(temp)


input = '''1227
1065
329
1063
1889
1700
1805
1373
389
1263
1276
1136
1652
1981
1406
1249
1197
1379
1050
1791
1703
2001
1842
1707
1486
1204
1821
1807
1712
1871
1599
1390
1219
1612
1980
1857
1511
1702
1455
1303
1052
1754
1545
1488
1848
1236
1549
1887
1970
1123
1686
1404
1688
1106
1296
401
1829
1693
1389
1957
914
1176
1348
1275
1624
1401
1045
1396
1352
1569
1060
1235
1679
1503
1340
1872
1410
1077
958
1681
1189
1466
1087
1852
1293
1139
1300
1323
661
1388
1983
1325
1112
1774
1858
1785
1616
1255
1198
1354
1124
1834
1417
1918
1496
33
1150
1861
1172
2006
1199
1558
1919
1620
1613
1710
1477
1592
1709
1909
1670
1922
1840
1768
1982
1193
1736
1877
1770
1191
1433
1072
1148
1225
1147
1171
1424
1913
1228
1339
1814
1504
1251
1240
1272
1500
1927
1428
1641
1453
1729
1976
1808
1180
1024
1108
1085
1669
1636
1005
1520
1929
1626
1551
1234
1988
1256
1524
1571
1506
1977
1749
1408
1540
1934
1810
1328
1910
1478
1600
1699
1413
1446
1798
1013
1998
1661
1058
1051
1220
1447
1675
1912
1668
1932
1962
1055
1757
1116
1090'''

input = input.split()
for i in input:
    lst.append(int(i))
# print (lst)

sort(lst)
print(lst)
result = find(lst, 2020)
print (result)
if (result is not None):
    print (result[0] * result[1])
else:
    print ("No solution, give me better inputs (`_`)")