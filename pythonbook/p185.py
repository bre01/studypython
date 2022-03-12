with open('p185.txt','a') as object:
    for i in range(100,int(2**9)):
        object.writelines(str(i)+'\n')
