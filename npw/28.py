class Dog():

	def __init__(self,name,age):
		'''初始化属性'''
		self.name=name
		self.age=age 
	def sit(self):
		'''小狗被命令时蹲下'''
		print(self.name.title()+' is now sitting.')
	def roll_over(self):
		print(self.name.tile()+' rolled over!')


my_dog = Dog('willie', 6)
print(my_dog.name.title())
	
my_dog.sit()
your_dog= Dog('lucy',9)

your_dog.sit()