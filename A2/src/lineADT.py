## @file lineADT.py
#  @title lineADT
#  @author Meet Patel
#  @date 2/27/2017

from math import *
from pointADT import *

## @brief This class represents a line as an abstract data type
#  @details This class includes functions that can be performed on the line object.
#  It uses values b and e which are the first and second points of the line respectively.
class LineT:
    
## @brief Constructor for LineT
#  @details Constructor accepts two parameters of type point for beginning and end points.
#  @param p1 is the first point of the line
#  @param p2 is the second point of the line
    def __init__(self, p1, p2):
        self.b = p1
        self.e = p2
        
## @brief Returns point object for beginning point of the line
#  @return beginning point, b, of the line
    def beg(self):
        return self.b

## @brief Returns point object for ending point of the line
#  @return ending point, e, of the line
    def end(self):
        return self.e
    
## @brief Returns length between line created by 2 points
#  @details Function uses distance method from pointADT
#  @return distance between two points
    def len(self):
        return self.b.dist(self.e)
    
## @brief Returns midpoint of the line as a point object
#  @details PointT object (midpoint) is created by using average of both existing points'
#  x and y coordinates. Local function avg takes in two values and divides by 2.0
#  to get a float number average
#  @return point object for midpoint of created line
    def mdpt(self):
        def __avg__(x1,x2):
            return (x1 + x2)/2.0
        return PointT(__avg__(self.b.xcrd(), self.e.xcrd()), __avg__(self.b.ycrd(), self.e.ycrd()))

## @brief Rotates points of line around axis by phi radians
#  @details Uses rot method from pointADT to rotate both points in line
#  which ends up rotating the line
#  @param phi is radians the point should be rotated by
    def rot(self, phi):
        self.b.rot(phi)
        self.e.rot(phi)



