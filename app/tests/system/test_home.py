from unittest import TestCase
from app import app

class TestHime(TestCase):
    def test_home(self):
        with app.test_client() as c:
            req = c.get('/')
