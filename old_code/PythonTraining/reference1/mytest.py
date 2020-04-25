from pkg.MyInt import MyInt 
import unittest 
class MyTest(unittest.TestCase):
    def test_add(self):
        """Testing add functionality"""
        a = MyInt(2)
        b = MyInt(3)
        c = a+b
        self.assertEqual(c, MyInt(5))
    def test_less(self):
        """Testing less functionality"""
        a = MyInt(2)
        b = MyInt(3)
        self.assertLess(a,b)