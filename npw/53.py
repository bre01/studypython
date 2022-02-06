import json 
def get_stored_username():
	filename='username.json'
	try:
		with open(filename) as ob:
			username=json.load(ob)
	except FileNotFoundError:
		return None 
	else:
		return username
print(get_stored_username())