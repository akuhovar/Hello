import unittest
import test_hello

def suite():
    suite = unittest.TestSuite()
    suite.addTest(test_hello.TestHello('test_name'))
    suite.addTest(test_hello.TestHello('test_no_name'))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())