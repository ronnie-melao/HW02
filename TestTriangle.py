# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(5,12,13),'Right','5,12,13 is a Right triangle')
        self.assertEqual(classifyTriangle(7,24,25),'Right','7,24,25 is a Right triangle')
        self.assertEqual(classifyTriangle(8,15,17),'Right','8,15,17 is a Right triangle')
        self.assertEqual(classifyTriangle(9,40,41),'Right','9,40,41 is a Right triangle')
        self.assertEqual(classifyTriangle(11,60,61),'Right','11,60,61 is a Right triangle')
        self.assertEqual(classifyTriangle(12,35,37),'Right','12,35,37 is a Right triangle')
        self.assertEqual(classifyTriangle(13,84,85),'Right','13,84,85 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        self.assertEqual(classifyTriangle(12,5,13),'Right','12,5,13 is a Right triangle')
        self.assertEqual(classifyTriangle(25,24,7),'Right','25,24,7 is a Right triangle')
        self.assertEqual(classifyTriangle(15,17,8),'Right','15,17,8 is a Right triangle')
        self.assertEqual(classifyTriangle(41,9,40),'Right','41,9,40 is a Right triangle')
        self.assertEqual(classifyTriangle(60,11,61),'Right','60,11,61 is a Right triangle')
        self.assertEqual(classifyTriangle(12,37,35),'Right','12,37,35 is a Right triangle')
        self.assertEqual(classifyTriangle(85,84,13),'Right','85,84,13 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertEqual(classifyTriangle(2,2,2),'Equilateral','2,2,2 should be equilateral')
        self.assertEqual(classifyTriangle(5,5,5),'Equilateral','5,5,5 should be equilateral')
        self.assertEqual(classifyTriangle(10,10,10),'Equilateral','10,10,10 should be equilateral')
        self.assertEqual(classifyTriangle(35,35,35),'Equilateral','35,35,35 should be equilateral')
        self.assertEqual(classifyTriangle(67,67,67),'Equilateral','67,67,67 should be equilateral')
        self.assertEqual(classifyTriangle(100,100,100),'Equilateral','100,100,100 should be equilateral')

    def testIsocelesTriangles(self): 
        self.assertEqual(classifyTriangle(1,2,2),'Isoceles','1,2,2 should be isoceles')
        self.assertEqual(classifyTriangle(2,2,1),'Isoceles','2,2,1 should be isoceles')
        self.assertEqual(classifyTriangle(3,5,5),'Isoceles','3,5,5 should be isoceles')
        self.assertEqual(classifyTriangle(100,100,101),'Isoceles','100,100,101 should be isoceles')
        self.assertEqual(classifyTriangle(3,2,3),'Isoceles','3,2,3 should be isoceles')
        self.assertEqual(classifyTriangle(12,2,12),'Isoceles','12,2,12 should be isoceles')

    def testScaleneTriangles(self): 
        self.assertEqual(classifyTriangle(1,2,3),'Scalene','1,2,3 should be scalene')
        self.assertEqual(classifyTriangle(3,1,2),'Scalene','3,1,2 should be scalene')
        self.assertEqual(classifyTriangle(5,2,9),'Scalene','5,2,9 should be scalene')
        self.assertEqual(classifyTriangle(100,101,102),'Scalene','100,101,102 should be scalene')
        self.assertEqual(classifyTriangle(5,7,9),'Scalene','5,7,9 should be scalene')
        self.assertEqual(classifyTriangle(32,11,29),'Scalene','32,11,29 should be scalene')

    def testNotATriangle(self): 
        self.assertEqual(classifyTriangle(1,1,100),'NotATriangle','1,1,100 is not a triangle')
        self.assertEqual(classifyTriangle(2,2,50),'NotATriangle','2,2,50 is not a triangle')
        self.assertEqual(classifyTriangle(3,5,100),'NotATriangle','3,5,100 is not a triangle')
        self.assertEqual(classifyTriangle(1000,100,10),'NotATriangle','1000,100,10 is not a triangle')
        self.assertEqual(classifyTriangle(123,456,789),'NotATriangle','123,456,789 is not a triangle')
        self.assertEqual(classifyTriangle(2,10,100),'NotATriangle','2,10,100 is not a triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()