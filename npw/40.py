filename='programming.txt'
with open(filename,'w') as file_object:
	file_object.write('I love programming\n')
	file_object.write('I love programming\n')
	file_object.write('I love programming\n')
	file_object.write('I love programming\n')
	for number in range(1,100):
		file_object.write('I love programming\n')


print('do')