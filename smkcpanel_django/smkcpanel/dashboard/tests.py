"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase, Client

class DashboardTestCase(TestCase):

	def setUp(self):
		# Every test needs a client.
		self.client = Client()

	def test_dashboard_home_basic_access(self):

		# Issue a GET request.
		response = self.client.get('/server/')

		# Check that the rendered content contains 'Aloha, My Friend!'
		text = 'Aloha, My Friend!'
		self.assertContains(response, text, count=None, status_code=200)



	def test_dashboard_say_my_name_default(self):

		# Issue a GET request.
		response = self.client.get('/server/say_my_name/PutYouNameHere')

		# Check that the rendered content contains 'Aloha, My Friend!'
		text = 'Hello, PutYouNameHere !'
		self.assertContains(response, text, count=None, status_code=200)


	def test_dashboard_say_my_name_specific(self):

		# Issue a GET request.
		response = self.client.get('/server/say_my_name/smk')

		# Check that the rendered content contains 'Aloha, My Friend!'
		text = 'Hello, smk !'
		self.assertContains(response, text, count=None, status_code=200)



	def test_dashboard_say_my_name_Heisenberg_redirect(self):

		# Issue a GET request.
		response = self.client.get('/server/say_my_name/')

		expected_url = '/server/say_my_name/Heisenberg'

		# Check that the response is 200 OK.
		self.assertRedirects(response, expected_url, status_code=302, target_status_code=200)


	def test_dashboard_say_my_name_Heisenberg_page(self):

		# Issue a GET request.
		response = self.client.get('/server/say_my_name/Heisenberg')

		# Check that the rendered content contains 'Aloha, My Friend!'
		text = 'Hello, Heisenberg !'
		self.assertContains(response, text, count=None, status_code=200)

		# Check that the rendered content contains 'Aloha, My Friend!'
		text = 'Heisenberg is the smartest bad ever'
		self.assertContains(response, text, count=None, status_code=200)
