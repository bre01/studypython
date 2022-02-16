list=[9,3,4,5,2,1,7,6,8]
def quicksort(list):
    if len(list)<2:
        return list 
    else:
        middle=list[0]
        less=[i for i in list[1:] if i < middle]
        greater=[i for i in list[1:] if i >=middle]
        return quicksort(less)+[middle]+quicksort(greater)

print(quicksort(list))
import math 