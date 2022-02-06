filename='inpython.txt'
with open(filename) as file_object:
	
	contents=file_object.read()
	lines=file_object.readlines()##read 语句会全部读完，如果用两次，第二次就读不了
	print(contents.rstrip())
with open(filename) as file_object:
	
	
	lines=file_object.readlines()##read 语句会全部读完，如果用两次，第二次就读不了
	
things=''
for line in lines:
	things+=line.rstrip() 
	print(line.rstrip())


print(things)

print(things.replace('write','readd'))