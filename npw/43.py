filename='userinfo1.txt'
with open(filename,'a') as file_object:
	while True:
		info=input('Enter your name ')
		if info:
			file_object.write('has been here\n')
			print('Hello '+info.title())
		else:
			break 
