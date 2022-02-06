import json 
number=[2,3,5,7,9,13]
filename='numbers.json'
with open(filename,'w') as ob:
	json.dump(number,ob)