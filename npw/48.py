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

def greet_user():
	username=get_stored_username()
	if username:
		print('hello '+username)
	else:
		username=get_new_username()
		
		print('we will remember you next time')

def get_new_username():
	username=input('Enter your username')
	with open ('username.json','a')as ob:
		json.dump(username,ob)
	return username 
		



greet_user()
wait=input('enter any key to quit')
