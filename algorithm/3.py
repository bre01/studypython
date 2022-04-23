import math
list=[1,3,5,7,9,11,13,15,17,19,21,23,25,27]
def bise(list,item):
    high=len(list)
    low=0
    mid=(low+high)//2
    while list[mid]!=item:
        if list[mid]>item:
            high=mid
            mid=(low+high)//2
        else:
            low=mid
            mid=(low+high)//2
    return mid+1
for i in list:

    print(bise(list,i))

for i in range(10):
    list.append(i)

print(math.cos(3.14159))