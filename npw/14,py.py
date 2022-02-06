def get_formatted_name(first,last,middle=''):
	if middle:
		print(first+middle+last)
	else:
		print(first+' '+last)

name=get_formatted_name('lily','james')
print(name)