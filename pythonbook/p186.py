object=open('p186.txt','r')
ls=object.readlines()
object.close()
print(ls)

newfile=open('newp186.txt','w+')

newfile.writelines(ls)
newfile.seek(0)
for line in newfile: 
    print(line)