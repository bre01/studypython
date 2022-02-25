import os 
print([x*x for x in range(1,11) if x%2==0 ] )
print([a+b for a in 'abc' for b in 'def'])
print([d for d in os.listdir('.')])
d = {'x': 'A', 'y': 'B', 'z': 'C' } 
for k,v in d.items():
    print(k+'='+v)
    print(k,'+',v,sep='')

print([v+' '+k for v,k in d.items()])
L = ['Hello', 'World  ', 'IBM', 'Apple'] 
print([s.rstrip() for s in L])#
print([x if x%2==0 else -x for x in range(1,11)])
L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[x.lower() for x in L1 if isinstance(x,str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')