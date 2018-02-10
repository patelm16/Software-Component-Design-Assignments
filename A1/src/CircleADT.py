## @file CircleADT.py
#  @title CircleADT
#  @author Meet Patel
#  @date 1/28/2017

import math

## @brief This class represents a circle
#  @details This class includes functions that can be performed on the circle
#  object. It has values x, y, and r where x and y represent the coordinates of
#  the centre point of the circle and r represents the radius of the circle.
class CircleT:

## @brief Constructor for CircleADT
#  @details Constuctor accepts three parameters for x-coordinate, y-coordinate, and radius.
#  @param x is the x-coordinate of the centre point of the circle
#  @param y is the y-coordinate of the centre point of the circle
#  @param r is the radius of the circle
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

## @brief Returns x-coordinate of the centre point of the circle
#  @return x-coordinate of the centre point of the circle
    def xcoord(self):
        return self.x

## @brief Returns y-coordinate of the centre point of the circle
#  @return y-coordinate of the centre point of the circle
    def ycoord(self):
        return self.y

## @brief Returns the radius of the circle
#  @return radius of the circle
    def radius(self):
        return self.r
    
## @brief This function calculates the area of the circle
#  @return Area of the circle
    def area(self):
        return math.pi * self.r**2

## @brief This function calculates the circumference of the circle
#  @return Circumference of the circle
    def circumference(self):
        return 2*math.pi*self.r


## @brief This function checks if the circle is inside a box
#  @details Using inputs 'xo', 'yo', 'w', and 'h', a box is created
#  @details Assumed that a circle's edges touching the edges of the box are considered inside the box
#  @param xo is the x coordinate of the left side of the box
#  @param yo is the y coordinate of the top of the box
#  @param w is the width of the box
#  @param h is the height of the box
#  @return Boolean value of true or false of whether the circle is inside the box
    def insideBox(self, xo, yo, w, h):
        if (self.r + self.x <= xo + w and self.x - self.r >= xo):
            if (self.y + self.r <= yo + h and self.y - self.r >= yo):
                return True
        return False

## @brief This function checks if two circles are intersecting
#  @details Two circles are intersecting if they share at least one point.
#  @details Another circle object is used to compare the common point(s) with
#  @param circle2 is the other circle object which the first circle object is comparing with
#  @return Boolean value of true or false of whether the two circles intersect
    def intersect(self, circle2):
        if (math.sqrt((self.x - circle2.x)**2 + (self.y - circle2.y)**2) < self.r + circle2.r):
            return True
        return False

## @brief This function scales the radius of a circle
#  @param k is the scaling factor of the radius
    def scale(self, k):
        self.r = k * self.r

## @brief This function translates the centre point (x and y coordinates) of a circle object
#  @param dx is the translation value of the centre point of the circle in the x direction
#  @param dy is the translation value of the centre point of the circle in the y direction
    def translate(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    
