class User():
	def __init__(self,first_name,last_name,age):
		self.name=last_name+first_name
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


user=User('quan','zhou','19')
user.describe()
user.greet()
user.update_login_times(6)
print(user.login_attempts)
user.reset_login_time()
print(user.login_attempts)