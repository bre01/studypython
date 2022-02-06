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


class IceCreamStand(Restaurant):
	def __init__(self,name,cuisine):
		super().__init__(name,cuisine)
		self.favours=['stawbarry','milk','apple']
	def show_ice(self):
		for favour in self.favours:
			print(favour+' icecream is dilicious!!')


mine=IceCreamStand('mike','forzen')
mine.show_ice()
print(mine.favours)
mine.describe_restaurant()
mine.open_restaurant()
mine.update_number(8)
print(mine.number_served)



