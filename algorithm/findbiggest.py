def findbiggest(list):
    if len(list)==0:
        return None
    biggest=list[0]
    if len(list)==1:
        return list[0]  
    else:
        if biggest >findbiggest(list[1:]):
            return biggest
        else:
            return findbiggest(list[1:])

print(findbiggest([1,3,334,552334,235,43,5,43,4321,3,12,4,32,5,34,5,3463242124,2,5,352321314,3432,4,1]))
print(findbiggest([1,3,34,2,5,56,6,4,43,6,6,4,6,3,]))
print(findbiggest([]))