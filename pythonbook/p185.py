with open('p185.txt','a') as object:
    for i in range(100,int(1.2e10)):
        object.writelines(str(i)+'\n')
