import json
def readbook():
	filename='book.json'
	try:
		with open(filename) as obj:
			book=json.load(obj)# a big problem about saving files !!!!
	except FileNotFoundError:
		book=input('enter your favourite book')
		with open(filename,'w') as ob:
			json.dump(book,ob)
		
		return book
	else:
		return book


print(readbook())
wait=input('any key')