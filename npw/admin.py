class User():
	def __init__(self,first_name,last_name,age):
		self.name=last_name+' '+first_name
		self.age=age
		self.login_attempts=0 
	def describe(self):
		print('Your name is '+self.name)
		print('your age is ' +self.age)
	def greet(self):
		print('good morning '+ self.name)
	def update_login_times(self,time):
		self.login_attempts += time 
	def add_login_times(self):
		self.login_attempts+=1 
	def reset_login_time(self):
		self.login_attempts=0 



class Privileges():
	def __init__(self):
		self.privileges=["can add post" ,"can delete post" ,"can ban user"]
	def showprivileges(self):
		for privilege in self.privileges:
			print('you can do ',privilege)


class Admin(User):
	def __init__(self,first_name,last_name,age):
		super().__init__(first_name,last_name,age)
		self.privilege=Privileges()

	



admin=Admin('quan','zhou',19)
admin.privilege.showprivileges()