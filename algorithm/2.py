my_list=[1,3,5,7,9,11,13,15,17,19,21,23,25,27]
def binary_search(list,item):
    length=len(list)
    index=length//2
    while my_list[index] != item:
        if my_list[index]>item:
                        
            index=index//2
            
        else:
            index= (index+length) // 2
            
    return index+1

change=[1,3,7,9,11,13,15,17,19,21,25,27]
for i in change:
    print(binary_search(change,i))
    

    


