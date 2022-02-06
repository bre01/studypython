filename='programming.txt'
with open(filename,'a') as file_object:
	file_object.write('i love to create something interesting\n')
	file_object.write('which makes me happy')
filename='userinfo.txt'
with open(filename,'a') as file_object2:
	while True:
		info=input('enter you name')
		print('hello ',info)
		file_object2.write(info,'has been here')
