def count_words(filename):
	'''calculate how many words in a book'''
	try:
		with open(filename) as ob:
			contents=ob.read()
	except FileNotFoundError:
		pass
	else:
		print(len(contents.split()))
count_words('reason.txt')

filenames=['reason.txt','userinfo.txt','userinfo1.txt','inpython.txt','doesntexsit.txt']
for filename in filenames:
	count_words(filename)