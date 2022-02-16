from itertools import count


def countdown(i):
    print(i)
    #占用大量的内存
    print(4)
    
    countdown(i-1)

countdown(7)

def fact(x):
    if x==1:
        return 1 
    else:
        return x*fact(x-1)

print(fact(3))
