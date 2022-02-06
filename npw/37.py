with open('pi_digits.txt')as file_object:
	lines=file_object.readlines()
pi=''
for line in lines:
	pi+=line.strip() 
print(float(pi))
print(len(pi))
print(pi)