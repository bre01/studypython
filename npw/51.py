import json


def saybook():
	filename='book.json'
	try:
		with open(filename) as obj:
			boo=json.load(obj)
	except FileNotFoundError:
		book=input('enter your book')
		with open(filename,'w') as ob:
			json.dump(book,ob)
		return None
	else:
		return boo
saybook()
wait=input('ente any key to quit')

