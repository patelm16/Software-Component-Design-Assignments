## @file circleADT.py
#  @title circleADT
#  @author Jenny Feng Chen (fengchej)
#  @date 2/19/2017

from pointADT import*
from lineADT import*
import math

## @brief This class represents a circle.
#  @details This class represent a circle with a center represented by PointT and a radius.
class CircleT(object):

    ## @brief This is a constructor for CircleT.
    #  @details This is a constructor for CircleT that takes two parameters and assigns one to center of circle and the radius of circle.
    #  @param cin is an instance of PointT object.
    #  @param rin is a positive real number.
    def __init__(self, cin, rin):
        self.c = cin
        self.r = float(rin)

    ## @brief This method returns the center point of the circle.
    #  @return the center of the circle.
    def cen(self):
        return self.c
    
    ## @brief This method returns the radius of the circle.
    #  @return the radius of the circle.
    def rad(self):
        return self.r

    ## @brief This method determines the area of the circle.
    #  @return the area of the circle.
    def area(self):
        return self.r**2 * math.pi

    ## @brief This method check whether two circles intersect.
    #  @details This method treat circles as filled objects. The set of points in each circle
    #  includes the boundary (closed sets).
    #  @param ci is an instance of the CircleT.
    #  @return true if the circles intersect; false if not.
    def intersect(self,ci):
        intersect = (self.cen().xcrd()-ci.cen().xcrd())**2 + (self.cen().ycrd()-ci.cen().ycrd())**2 <= (self.rad() + ci.rad())**2
        return intersect

    ## @brief This method creates a new line between the center of two circles.
    #  @param ci is an instance of the circle.
    #  @return line which is a new instance of the LineT object.
    def connection(self, ci):
        return LineT(self.cen(), ci.cen())

    ## @brief This method calculates the gravitational force between two circles.
    #  @details This method takes a function and return a function. It is basically calculates the gravitational force between two circles using the universal gravitational constant.
    #  @param f is a function that takes a real number an returns a real number.
    #  @return f1 a function that takes an instance of CircleT and returns a real number.
    def force(self, f):    
        f1 = lambda x: x.area()*self.area()* f(self.connection(x).len())
        return f1
