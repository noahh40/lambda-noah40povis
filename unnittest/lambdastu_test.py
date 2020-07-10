#!/usr/bin/env python

import unittest 
import lambdastu
#from lambdastu import Lambdastudents, DataSci

class TestLambdastudents(unittest.TestCase):
    def testcode(self):
        user1 = lambdastu.DataSci('Cook','Rob', 34, 16)
        user2 = lambdastu.DataSci('Student','Noah',26,16)
        self.assertEqual(user1.age, 34)
        self.assertEqual(user2.age, 25)
        return "All test pass successfully."

if __name__ =='__main__':
    unittest.main()


