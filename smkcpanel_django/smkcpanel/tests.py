# """
# This file demonstrates writing tests using the unittest module. These will pass
# when you run "manage.py test".

# Replace this with more appropriate tests for your application.
# """

# from django.test import TestCase, Client

# class StaticFilesTestCase(TestCase):
# 	"""docstring for StaticFilesTestCase"""
# 	def setUp(self):
# 		# Every test needs a client.
# 		self.client = Client()

# 	def test_bootstrap_css(self):
# 		# Issue a GET request.
# 		response = self.client.get('/static/bootstrap/extra/bootswatch/cerulean/css/bootstrap.css')

# 		# Check that the response is 200 OK.
# 		self.assertEqual(response.status_code, 200)
		

# 	def test_bootstrap_css_min(self):
# 		# Issue a GET request.
# 		response = self.client.get('/static/bootstrap/extra/bootswatch/cerulean/css/bootstrap.min.css')

# 		# Check that the response is 200 OK.
# 		self.assertEqual(response.status_code, 200)


# 	def test_bootstrap_js_min(self):
# 		# Issue a GET request.
# 		response = self.client.get('/static/bootstrap/dist/js/bootstrap.min.js')

# 		# Check that the response is 200 OK.
# 		self.assertEqual(response.status_code, 200)


# 	def test_jquery_js(self):
# 		# Issue a GET request.
# 		response = self.client.get('/static/bootstrap/assets/js/jquery.js')

# 		# Check that the response is 200 OK.
# 		self.assertEqual(response.status_code, 200)

# 	def test_jquery_min_map(self):
# 		# Issue a GET request.
# 		response = self.client.get('/static/bootstrap/assets/js/jquery-1.10.2.min.map')

# 		# Check that the response is 200 OK.
# 		self.assertEqual(response.status_code, 200)


# 	def test_font_awesome_css(self):
# 		# Issue a GET request.
# 		response = self.client.get('/static/bootstrap/extra/font-awesome/css/font-awesome.min.css')

# 		# Check that the response is 200 OK.
# 		self.assertEqual(response.status_code, 200)


# 	def test_twitter_widgets_js(self):
# 		# Issue a GET request.
# 		response = self.client.get('/static/bootstrap/extra/twitter/widgets.js')

# 		# Check that the response is 200 OK.
# 		self.assertEqual(response.status_code, 200)