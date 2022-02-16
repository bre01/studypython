from findsmallest import findsmallest
def selectsort(arr):
    newarr=[]
    for i in range(len(arr)):
        newarr.append(arr.pop(findsmallest(arr)))
    return newarr
print(selectsort(([1,3,4,3,4,3,5213,12,312,3,12,31,32,24,32,5,43,6,546,54,])))