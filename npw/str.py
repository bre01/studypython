filename='srt.srt'
with open(filename) as file_object:
	lines=file_object.readlines()
pi_string=''
for line in lines:
	if '-->' in line:
		pass
	else:
		pi_string+=line + '\n'          


filename='newde'+filename
with open(filename,'w') as file_object:
	file_object.write(pi_string)