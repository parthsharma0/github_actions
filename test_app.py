# test_app.py
import unittest
from app import add

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 4), 7)

if __name__ == '__main__':
    unittest.main()
