from random import  randint,random

class Die():
	def __init__(self,sides=6):	
		self.sides=sides	
	def roll_die(self):
		print(randint(1,self.sides))
mine=Die(200)
mine.roll_die()
his=Die(100)
his.roll_die()