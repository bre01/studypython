def findMinAndMax(L):
    if len(L)==0:
        return None,None  
    min=L[0]
    for item in L:
        if item<min:
            min=item
    max=L[0]
    for item in L:
        if item>max:
            max=item 
    return(min,max)

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
        