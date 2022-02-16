def binary_search(list,item):
    low=0 
    high=len(list)-1
    while low<=high:
        mid=(low+high)//2
        guess = list[mid]
        if guess == item:
            return mid
            
        if guess >item:
            high=mid -1 
        else:
            low=mid+1

    return None
my_list=[1,3,5,7,9,11,13,15,17,19,21,23,25,27]
print(binary_search(my_list,23))


def dcbinary(list,item):
    low=0
    high=len(list)-1
    if low>high:
        return None
    mid=(low+high)//2 
     
    if item==list[mid]:
        return mid 
    else:
        if item< list[mid]:
            
            return dcbinary(list[:mid],item)
        else:
            return dcbinary(list[mid:],item)
print(dcbinary(my_list,23))

    