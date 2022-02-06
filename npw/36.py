with open('text_files/subfile.txt') as file_object:
	contents=file_object.read()
	print(contents.rstrip())
with open('text_files/subfile.txt') as file_object:
	for line in file_object:
		print(line.rstrip())