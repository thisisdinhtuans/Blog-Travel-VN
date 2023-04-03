from django.test import TestCase, SimpleTestCase

# Create your tests here.
class SimpleTest(SimpleTestCase):
    def test_home_page_status(self):
        response=self.client.get('/')#client get đến cái đường dẫn trắng, chính là path('') (ở urls.py) 
        self.asertEquals(response.status_code, 200) #xem cái này nó có bằng 200 không