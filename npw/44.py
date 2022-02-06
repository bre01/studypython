filename='reason.txt'
while True:
	reason=input('why you learn programming?')
	if reason:
		with open(filename,'a') as file:
			file.write(reason+'\n')
	else:
		break

print("i don't know how to describe it??")   