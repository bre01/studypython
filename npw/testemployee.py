import unittest
from employee import Employee 
class TestAnonymousSurvey(unittest.TestCase):

	def setUp(self):
		self.amy=Employee('amy','james',1000)
	def testdefault(self):
		ori=self.amy.salary
		self.amy.give_raise()
		self.assertEqual(self.amy.salary-ori,5000)
	def testgive(self):
		ori=self.amy.salary
		self.amy.give_raise(1223)
		self.assertEqual(self.amy.salary-ori,1223)

unittest.main()