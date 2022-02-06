def get_formatted_name(first,last,middle=''):
	if middle:
		return first+' '+middle+' '+last
	else:
		return first+' '+last

name=get_formatted_name('lily','james')
print(name)
print(get_formatted_name('lily','james','willian'))
