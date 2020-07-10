#!/usr/bin/env python

# Create Unittests for both modules
# Make sure each class/method includes a docstring
# Make sure entire script conforms to PEP8 guidelines
# To test, run the script in the terminal.


# Standard Python Library
import unittest

# Local Imports
from puppy import Puppy, Leech
from arithmetic import SimpleOperations, Complex


case1 = SimpleOperations(3, 2)
case2 = Complex(3, 2)



class ArithmeticTest(unittest.TestCase):
    # TODO
    def test_arith(self):
        x = case1.add()
        a = case1.multiply()
        b = case1.subtract()
        c = case1.divide()
        self.assertEqual(x, 5)

        self.assertEqual(a, 6)

        self.assertEqual(b, 1)

        self.assertEqual(c, 1.5)

    def test_complex(self):
        z = case2.exponentiation()

        p = case2.nth_root()

        self.assertEqual(z, 9)
        
        self.assertEqual(p, 1.7320508075688772)

case3 = Puppy('James', 5)
case4 = Leech('Jonathan', 10, True)

class PuppyTest(unittest.TestCase):
    
    def test_dog(self):

       

        self.assertEqual(case3.name,'James')
        self.assertEqual(case3.age, 5)
        self.assertEqual(case4.is_hypoallergenic, True)



if __name__ == "__main__":
    unittest.main()
