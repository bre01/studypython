filename='userinfo.txt'
while True:
	info=''
	info=input('enter you name')	
	print('hello '+info)
	with open(filename,'a') as file_object:
		file_object.write(info+'has been here\n')

#这样子可以自己关闭文件 如果间循环放在里面可能导致数据丢失
wait=input()
	

