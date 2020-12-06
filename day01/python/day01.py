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
    
def find3Numbers(lst, arr_size, sum):
    for i in range(0, arr_size-2):
        l = i + 1 
          
        # index of the last element 
        r = arr_size-1 
        while (l < r): 
          
            if( lst[i] + lst[l] + lst[r] == sum): 
                result = [lst[i], lst[l], lst[r]]
                return result
              
            elif (lst[i] + lst[l] + lst[r] < sum): 
                l += 1
            else: # A[i] + A[l] + A[r] > sum 
                r -= 1
  
    # If we reach here, then 
    # no triplet was found 
    return None
        
        
lst = list()

choice = input("Do you want to provide custom input(y or Y): ")
if choice == 'y' or choice == 'Y':
    while (True) :
        temp = input('Input Numbers: ')
        if len(temp) < 1 : break
        temp = int(temp)
        lst.append(temp)
else:
    fhand = open('../input.txt')
    for line in fhand:
        lst.append(int(line.rstrip()))
    
# print (lst)

sort(lst)
print(lst)
result = find3Numbers(lst, len(lst), 2020)
print (result)
if (result is not None):
    print (result[0] * result[1] * result[2])
else:
    print ("No solution, give me better inputs (`_`)")