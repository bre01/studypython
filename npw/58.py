from survey import AnonymousSurvey
import unittest 

class TestAnonymousSurvey(unittest.TestCase):
	''''''
	def  test_store_response(self):
		''''''
		question='which one'
		my_survey=AnonymousSurvey(question)
		my_survey.store_response('english')
		self.assertIn('english',my_survey.responses)
	def test_multiple_response(self):
		''''''
		question='which one'
		my_survey=AnonymousSurvey(question)
		
		answers=['love','and','sex','affection']
		for answer in answers:
			my_survey.store_response(answer)
		for answer in answers:
			self.assertIn(answer,my_survey.responses)


unittest.main()
