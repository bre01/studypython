class Employee():
	def __init__(self,firstname,lastname,salary):
		self.name=firstname+''+lastname
		self.salary=salary 
	def give_raise(self,money=5000):
		self.salary  += money 

lily=Employee('lily','james',30000)
lily.give_raise()
print(lily.salary)
lily.give_raise(8999)
print(lily.salary)
