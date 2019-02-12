import sys
sys.path.append('..')
sys.path.append('.')
import hello
import unittest

class TestHello(unittest.TestCase):
    def test_name(self):
        for name, greeting in zip(("Anton", "Антон"),("Hello, Anton!", "Hello, Антон!")):
            hw = hello.HelloWorld(name)
            self.assertEqual(hw.greeting(), greeting)
    def test_no_name(self):
        name = None
        hw = hello.HelloWorld(name)
        self.assertIsNone(hw.name)
        self.assertEqual(hw.greeting(), "")    

if __name__ == "__main__":
    unittest.main()
