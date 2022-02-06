import json 
filename='numbers.json'
with open(filename) as ob:
	numbers=json.load(ob)
for number in numbers:
	print(number)