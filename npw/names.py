from name_function import get_formatted_name as name
print('enter q to quit')
while True:
	first=input('\n first name')
	if first=='q':
		break 
	last=input('\n last name')
	if last=='q':
		break 
	print(name(first,last))