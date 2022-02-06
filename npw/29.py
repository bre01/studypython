class Restaurant():
	def __init__(self,name,cuisine):
		self.restaurant_name=name
		self.cuisine_type=cuisine
		self.number_served=0
	def describe_restaurant(self):
		print('name is ',self.restaurant_name.title())
		print('cuisine is ',self.cuisine_type)
	def open_restaurant(self):
		print("it's open ")
	def update_number(self,number):
		self.number_served+=number 


my_restaurant=Restaurant('apple','chinese')
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

his_restaurant=Restaurant('yahoo','west')
her_restaurant=Restaurant('google','middle')

his_restaurant.describe_restaurant()
her_restaurant.describe_restaurant()
his_restaurant.update_number(6)
print(his_restaurant.number_served)