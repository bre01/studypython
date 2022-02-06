import unittest 
from survey import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):

	def setUp(self):
		question='which one'
		self.my_survey=AnonymousSurvey(question)
		self.responses=['english','madarin','spanish']
	def test_single(self):
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0],self.my_survey.responses)
	def test_multiple(self):
		for response in self.responses:
			self.my_survey.store_response(response)
		for response in self.responses:
			self.assertIn(response,self.my_survey.responses)

unittest.main()




