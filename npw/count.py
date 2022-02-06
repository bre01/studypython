with open ('inpython.txt' ) as ob:
	line =ob.read()
print(line.upper().count('python'))