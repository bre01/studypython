import json



def saybook():
	with open('book.json','w') as ob:
		book=json.load(ob)
	if book:
		print(book)
	else:
		book=input('enter your favourite book')
		json.dump(book,ob)
		ptint('i will know next time ')

	
saybook()
wait=input('any key')