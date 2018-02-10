## @file testCircles.py
#  @title TestCircles
#  @author Meet Patel
#  @date 1/28/2017

from CircleADT import *
from Statistics import *
import numpy

C1 = CircleT(3.0, 5.0, 5.0)
C2 = CircleT(13.0, 8.0, 9.0)
C3 = CircleT(7.0, 2.0, 4.0)
C4 = CircleT(-6.0, -8.0, 3.0)
C5 = CircleT(13.0, 8.0, 9.0)
C6 = CircleT(4.0, 5.0, 2.0)
C7 = CircleT(8.0, 4.5, 2.5)
C8 = CircleT(3.5, 2.5, 5.0)

## @brief Tests the x-coordinate getter
def xcoordTest():
    if (C1.xcoord() == 3.0):
        print "The xcoord method works correctly."
    else:
        print "The xcoord method does not work correctly."

## @brief Tests the y-coordinate getter
def ycoordTest():
    if (C2.ycoord() == 8.0):
        print "The ycoord method works correctly."
    else:
        print "The ycoord method does not work correctly."

## @brief Tests the radius value getter
def radiusTest():
    if (C3.radius() == 4.0):
        print "The radius method works correctly."
    else:
        print "The radius method does not work correctly."

## @brief Tests the area function from class CircleADT
def areaTest():
    if (C1.area() == 78.53981633974483):
        print "The area method works correctly."
    else:
        print "The area method does not work correctly."

## @brief Tests the circumference function from class CircleADT
def circumferenceTest():
    if (C1.circumference() == 31.41592653589793):
        print "The circumference method works correctly."
    else:
        print "The circumference method does not work correctly."

## @brief Tests the insideBox function from class CircleADT
#  @details Tests different possible cases of the function which includes:
#  the box inside the circle, the box outside the circle, and the box edges aligning with the circle's edges
def insideBoxTest():
    if (C6.insideBox(1,1,14,14)):
        print "The inside box method works when the circle is inside the box."
    else:
        print "The inside box method does not work correctly when the circle is inside the box."

    if (not C6.insideBox(4,6,5,2)):
        print "The inside box method works when the circle is not inside the box."
    else:
        print "The inside box method does not work correctly when the circle is not inside the box."

    if (C6.insideBox(2,3,4,4)):
        print "The inside box method works when the circle's edges are touching the box's edges."
    else:
        print "The inside box method does not work correctly when the circle's edges are touching the box's edges."

## @brief Tests the intersect function from class CircleADT
#  @details Tests different possible cases of the function which includes:
#  the circles on top of each other, one circle inside another, two circles with no common points
def intersectTest():
    if (C2.intersect(C1)):
        print "The intersect method works when one circle is inside another."
    else:
        print "The intersect method does not work when one circle is inside another."

    if (not C2.intersect(C4)):
        print "The intersect method works when the two circles do not have any points in common."
    else:
        print "The intersect method does not work correctly when the two circles do not have any points in common."

    if (C2.intersect(C5)):
        print "The intersect method works when two circles are lined up on top of each other."
    else:
        print "The intersect method does not work when two circles are lined up on top of each other."

## @brief Tests the scale function from the class CircleADT
#  @details Uses an appropriate 'k' value to test if the outputted radius is correct
def scaleTest():
    C7.scale(3.0)
    if (C7.radius() == 7.5):
        print "The scale method works correctly."
    else:
        print "The scale method does not work correctly."

## @brief Tests the translate function from the class CircleADT
#  @details Uses an appropriate 'dx' and 'dy' values to test if the
#  outputted x and y coordinates are correctly translated
def translateTest():
    C7.translate(3.0, 5.0)
    if (C7.xcoord() == 11.0 and C7.ycoord() == 9.5):
        print "The translate method works correctly with positive inputs."
    else:
        print "The translate method does not work correctly with positive inputs."

    C8.translate(-4.0, -6.0)
    if (C8.xcoord() == -0.5 and C8.ycoord() == -3.5):
        print "The translate method works correctly with negative inputs."
    else:
        print "The translate method does not work correctly with negative inputs."

## @brief Tests the average function from Statistics
#  @details Takes in a list of circles to verify that
#  outputted average value is correct
def averageTest():
    if (average([C1, C2, C3, C4]) == 5.25):
        print "The average method works correctly."
    else:
        print "The average method does not work correctly."

## @brief Tests the stdDev function from Statistics
#  @details Takes in a list of circles to verify that
#  outputted standard deviation value is correct
def stdDevTest():
    if (stdDev([C1, C2, C3, C4]) == 2.2776083947860748):
        print "The stdDev method works correctly."
    else:
        print "The stdDev method does not work correctly."

## @brief Tests the rank function from Statistics
#  @details Takes in a list of circles to verify that the outputted
#  list is correctly ranked. Tests a list of circles with all
#  unique radii and one with a repeated radius
def rankTest():
    if (rank([C1,C2,C3,C4,C6]) == [2,1,3,4,5]):
        print "The rank method works correctly with 5 different radii in the list."
    else:
        print "The rank method does not work correctly with all different radii in the list."

    if (rank([C1,C2,C3,C4,C5]) == [3,1,4,5,1]):
        print "The rank method works correctly with a repeated radius in the list."
    else:
        print "The rank method does not work correctly with a repeated radius in the list."

xcoordTest()
ycoordTest()
radiusTest()
areaTest()
circumferenceTest()
insideBoxTest()
intersectTest()
scaleTest()
translateTest()
averageTest()
stdDevTest()
rankTest()
