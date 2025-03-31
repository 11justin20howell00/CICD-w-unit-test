# test_hello.py
import unittest
from hello import hello

class TestHelloFunction(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "hello")

if __name__ == "__main__":
    unittest.main()
