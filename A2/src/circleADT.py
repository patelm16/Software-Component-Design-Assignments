## @file circleADT.py
#  @title circleADT
#  @author Meet Patel
#  @date 2/27/2017

from math import *
from pointADT import *
from lineADT import *

## @brief This class represents a circle
#  @details This class includes functions that can be performed on the circle
#  object. It represents the circle object with a center point (as PointT)
#  and a radius value.
class CircleT:

## @brief Constructor for CircleT
#  @details Constuctor accepts 2 parameters; one for the center of the circle
#  and one for the radius of the circle
#  @param c is the instance of the PointT object which represents the center point
#  @param r is radius of the circle represented as a real number
    def __init__(self, cin, rin):
        self.c = cin
        self.r = float(rin) 
        
## @brief Returns centre point of the circle
#  @return centre point of the circle
    def cen(self):
        return self.c

## @brief Returns radius of the circle
#  @return radius of the circle
    def rad(self):
        return self.r
    
## @brief This function calculates the area of the circle
#  @return area of the circle
    def area(self):
        return pi * self.r**2

## @brief This function checks if two circles are intersecting
#  @details Two circles are intersecting if they share at least one point.
#  Assuming that points inside a circle and on border of circle are
#  a part of the circle.
#  @param ci is the other circle object (from CircleT) which the first circle
#  object is comparing with
#  @return Boolean value of true or false of whether the two circles intersect.
#  True is returned if they do intersect and false if they do not.
    def intersect(self, ci):
        return (self.cen().xcrd()-ci.cen().xcrd())**2 + (self.cen().ycrd()-ci.cen().ycrd())**2 <= (self.rad() + ci.rad())**2

## @brief This function makes a new line between centers of both circles.
#  @param ci is the other circle object from which to make the line from
#  @return Line created from centers of both circles as a LineT object.
    def connection(self, ci):
        return LineT(self.cen(), ci.cen())

## @brief This function calculates the gravitational force between two circles.
#  @details The force between two circles is calculated by using the function
#  f and the formula given in the assignment sheet
#  @param f is a function used to find force between the two circles
#  @return value of force between the two circles with given function
    def force(self, f):
        return lambda x: self.area()* x.area()*f(self.connection(x).len())
        
