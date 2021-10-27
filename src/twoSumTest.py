
'''
Created on Oct 26, 2021

@author: rishikasurineni
'''
 
import unittest
from twoSum import twoSum

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
class twoSumTest(unittest.TestCase):
    def test(self):
        #assert statements
        self.assertEqual(twoSum([2,7,11,15],9), [0,1])
        self.assertEqual(twoSum([3,2,4], 6), [1,2])
        