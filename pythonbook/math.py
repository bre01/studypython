import time 
import random 
scale=50
print('begin'.center(scale//2,'-'))
s= time.perf_counter() 
while scale>=0:
     
    time.sleep((random.randint(1,3)))
    print('\r {}%{}->{}'.format(100-scale*2,'-'*(50-scale),'-'*scale),end="")
    s=time.perf_counter()
    scale-=random.randint(1,20) 
    
print('\r {}%{}->{}'.format(100,'-'*(50),'-'*0),end="")
print()