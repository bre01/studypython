def sum(arr):
    sum=0
    while len(arr)!=0:
        sum += arr.pop()
    return sum
def sum2(arr):
    
    
    if len(arr)==0:
        return 0
        
            
    return   arr[0]+sum2(arr[1:])
def callen(list):
    if list==[]:
        return 0
    return 1+callen(list[1:])

def findbiggest(list):
    biggest=list[0]
    if len(list)==1:
        
        return list[0]
        
        
    else:
        if biggest> findbiggest(list[1:]):
            return biggest 
        else:
            return findbiggest(list[1:])


    
    
print(findbiggest([1,3,4,34,1235,2]))

print(callen([1,3,4,34,1235,2]))
print(sum2([1,3,4,34,1235,2]))
print(sum([1,3,4,34,35,2]))
