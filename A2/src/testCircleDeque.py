## @file testCirclesDeque.py
#  @title testCirclesDeque
#  @author Meet Patel, patelm16
#  @date 2/27/2017

import unittest
from circleADT import *
from deque import *
from pointADT import *
from lineADT import *

## @brief This class uses PyUnit Unittesting to test methods from the following
#  modules: pointADT.py, lineADt.py. circleADT.py, and deque.py
class testCirclesDeque(unittest.TestCase):

## @brief Initializes main objects and functions to be used in the testing
#  at the start of each test
    def setUp(self):
        self.p1 = PointT(2.0, 3.0)
        self.p2 = PointT(5.0,4.0)
        self.line1 = LineT(self.p1, self.p2)
        self.p5 = PointT(6.0, 9.0)
        self.c1 = CircleT(self.p5, 3.0)
        self.c2 = CircleT(self.p1, 8.0)
        self.c3 = CircleT(self.p2, 11.0)
        self.f = lambda r: 6.672*r**(-3)
        Deq.init()
        self.deq = Deq

## @brief Removes all values at the end of each test
    def tearDown(self):
        self.p1 = None
        self.p2 = None
        self.line1 = None
        self.p5 = None
        self.c1 = None
        self.c2 = None
        self.c3 = None
        self.f = None
        self.deq = None

## @brief tests the xcrd method from pointADT
    def test_xcrd_correct(self):
        self.assertTrue(self.p1.xcrd() == 2.0)
        
## @brief tests the ycrd method from pointADT
    def test_ycrd_correct(self):
        self.assertTrue(self.p1.ycrd() == 3.0)

## @brief tests the dist method from pointADT
    def test_dist_correct(self):
        self.assertTrue(self.p1.dist(self.p2) == 3.1622776601683795)

## @brief tests the rot method for positive inputs from pointADT
    def test_rot_PositiveInput_correct(self):
        self.p1.rot(3.14)
        self.assertTrue(self.p1.xcrd() == -2.0047754222045393 and self.p1.ycrd() == -3.0031891066056935)

## @brief tests the rot method for zero inputs from pointADT
    def test_rot_ZeroInput_correct(self):
        self.p1.rot(0)
        self.assertTrue(self.p1.xcrd() == 2.0 and self.p1.ycrd() == 3.0)

## @brief tests the rot method for negative inputs from pointADT
    def test_rot_NegativeInput_correct(self):
        self.p1.rot(-1.57)
        self.assertTrue(self.p1.xcrd() == 3.0015917022169702 and self.p1.ycrd() == -2.9992017703755964)

## @brief tests the rot method for inputs greater than pi from pointADT
    def test_rot_GreaterThanPiInput_correct(self):
        self.p1.rot(4.0)
        self.assertTrue(self.p1.xcrd() == 0.9631202441965605 and self.p1.ycrd() == -2.689822666680374)

## @brief tests the beg method from lineADT
    def test_beg_correct(self):
        self.assertTrue(self.line1.beg().xcrd() == 2.0 and self.line1.beg().ycrd() == 3.0)

## @brief tests the end method from lineADT
    def test_end_correct(self):
        self.assertTrue(self.line1.end().xcrd() == 5.0 and self.line1.end().ycrd() == 4.0)

## @brief tests the len method from lineADT
    def test_len_correct(self):
        self.assertTrue(self.line1.len() == 3.1622776601683795)

## @brief tests the mdpt method from lineADT with differerent inputs (length not equal to one)
    def test_mdpt_correct(self):
        self.assertTrue(self.line1.mdpt().xcrd() == 3.5 and self.line1.mdpt().ycrd() == 3.5)

## @brief tests the mdpt method from lineADT with a length of zero between points
    def test_mdpt_LengthZero_correct(self):
        p3 = PointT(8.0,8.0)
        p4 = PointT(8.0,8.0)
        line2 = LineT(p3,p4)
        self.assertTrue(line2.mdpt().xcrd() == 8.0 and line2.mdpt().ycrd() == 8.0)

## @brief tests the rot method from lineADT
    def test_rot_forLine_correct(self):
       self.line1.beg().rot(-0.6)
       self.line1.end().rot(2.3)
       self.assertTrue(self.line1.beg().xcrd() == 3.344598650004463 and self.line1.beg().ycrd() ==0.5875043904768189 and self.line1.end().xcrd() == -6.314200955106001  and self.line1.end().ycrd() == -7.373636648073067)

## @brief tests the cen method from circleADT
    def test_cen_correct(self):
        self.assertTrue(self.c1.cen().xcrd() == 6.0 and self.c1.cen().ycrd() == 9.0)

## @brief tests the rad method from circleADT
    def test_rad_correct(self):
        self.assertTrue(self.c1.rad() == 3.0)
        
## @brief tests the area method from circleADT
    def test_area_correct(self):
        self.assertTrue(self.c1.area() == 28.274333882308138)

## @brief tests the intersect method from circleADT
    def test_intersect_correct(self):
        self.assertTrue(self.c1.intersect(self.c2))

## @brief tests the connection method from circleADT
    def test_connection_correct(self):
        self.assertTrue(self.c1.connection(self.c2).beg().xcrd() == 6 and self.c1.connection(self.c2).beg().ycrd() == 9 and self.c1.connection(self.c2).end().xcrd() == 2 and self.c1.connection(self.c2).end().ycrd() == 3) 

## @brief tests the force method from circleADT
    def test_force_correct(self):
        self.assertTrue(self.c1.force(self.f)(self.c2) == 101.15171511042486)
        
## @brief tests the pushBack method from deque
    def test_pushBack_correct(self):
        self.deq.pushBack(self.c1)
        self.assertTrue(self.deq.s[0].cen().xcrd() == 6.0 and self.deq.s[0].cen().ycrd() == 9.0 and self.deq.s[0].rad() == 3.0)

## @brief tests the pushFront method from deque
    def test_pushFront_correct(self):
        self.deq.pushBack(self.c1)
        self.deq.pushFront(self.c2)
        self.assertTrue(self.deq.s[0].cen().xcrd() == 2.0 and self.deq.s[0].cen().ycrd() == 3.0 and self.deq.s[0].rad() == 8.0)

## @brief tests the pushFront method from deque with a full deque exception
    def test_pushFrontFullException_correct(self):
        for i in range(20):
            self.deq.pushFront(self.c1)
        self.assertRaises(FULL,self.deq.pushFront,self.c2)

## @brief tests the popFront method from deque with an empty deque exception
    def test_popFrontEmptyException_correct(self):
        self.assertRaises(EMPTY,self.deq.popFront)

## @brief tests the popBack method from deque
    def test_popBack_correct(self):
        self.deq.pushBack(self.c1)
        self.deq.pushBack(self.c2)
        self.deq.popBack()
        self.assertTrue(self.deq.s[0].cen().xcrd() == 6.0 and self.deq.s[0].cen().ycrd() == 9.0 and self.deq.s[0].rad() == 3.0)

## @brief tests the popFront method from deque
    def test_popFront_correct(self):
        self.deq.pushBack(self.c1)
        self.deq.pushBack(self.c2)
        self.deq.popFront()
        self.assertTrue(self.deq.s[0].cen().xcrd() == 2.0 and self.deq.s[0].cen().ycrd() == 3.0 and self.deq.s[0].rad() == 8.0)

## @brief tests the back method from deque
    def test_back_correct(self):
        self.deq.pushBack(self.c1)
        self.deq.pushBack(self.c2)
        self.assertTrue(self.deq.back().cen().xcrd() == 2.0 and self.deq.back().cen().ycrd() == 3.0 and self.deq.back().rad() == 8.0)

## @brief tests the front method from deque
    def test_front_correct(self):
        self.deq.pushBack(self.c1)
        self.deq.pushBack(self.c2)
        self.assertTrue(self.deq.front().cen().xcrd() == 6.0 and self.deq.front().cen().ycrd() == 9.0 and self.deq.front().rad() == 3.0)

## @brief tests the size method from deque
    def test_size_correct(self):
        self.deq.pushBack(self.c1)
        self.deq.pushBack(self.c2)
        self.deq.pushBack(self.c3)
        self.assertTrue(self.deq.size() == 3)
        
## @brief tests the disjoint method from deque with three different circles
    def test_disjoint_correct(self):
        self.deq.pushBack(self.c1)
        self.deq.pushBack(self.c2)
        self.deq.pushBack(self.c3)
        self.assertFalse(self.deq.disjoint())

## @brief tests the disjoint method from deque with one circle
    def test_disjoint_oneCircle_correct(self):
        self.deq.pushBack(self.c1)
        self.assertTrue(self.deq.disjoint())
    
## @brief tests the pushBack method from deque with an empty deque
    def test_disjoint_emptyException_correct(self):
        self.assertRaises(EMPTY,self.deq.disjoint)

## @brief tests the sumFx method from deque
    def test_sumFx_correct(self):
        self.deq.pushFront(self.c1)
        self.deq.pushFront(self.c2)
        self.deq.pushFront(self.c3)
        self.assertTrue(self.deq.sumFx(self.f) == -15192.191286940368 )

## @brief tests the totalArea method from deque
    def test_totalArea_correct(self):
        self.deq.pushBack(self.c1)
        self.deq.pushBack(self.c2)
        self.deq.pushBack(self.c3)
        self.assertTrue(self.deq.totalArea() == 609.4689747964198)

## @brief tests the averageRadius method from deque
    def test_averageRadius_correct(self):
        self.deq.pushBack(self.c1)
        self.deq.pushBack(self.c2)
        self.deq.pushBack(self.c3)
        self.assertTrue(self.deq.averageRadius() == 7.333333333333333)
 
print "All test cases from all modules have passed."
        
if __name__ == '__main__':
    unittest.main()


