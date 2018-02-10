## @file pointADT.py
#  @title pointADT
#  @author Meet Patel
#  @date 2/27/2017

from math import *

## @brief This class represents a point as an abstract data type
#  @details This class includes functions that can be performed on the point object.
#  It uses values xc and yc which are the x and y coordinates of the point respectively.
class PointT:

## @brief Constructor for PointT
#  @details Constructor accepts two parameters for the x and y coordinate of point
#  @param xc is the x coordinate of the point
#  @param yc is the y coordinate of the point
    def __init__(self, xc, yc):
        self.xc=float(xc)
        self.yc=float(yc)
        
## @brief Returns x-coordinate of the point 
#  @return x-coordinate of the point
    def xcrd(self):
        return self.xc

## @brief Returns y-coordinate of the point 
#  @return y-coordinate of the point
    def ycrd(self):
        return self.yc
    
## @brief Returns distance between 2 points using distance formula
#  @details Function takes in parameter p as the second point
#  @param p contains information on the second point
#  @return distance between 2 points
    def dist(self, p):
        return sqrt((self.xc - p.xcrd())**2 + (self.yc - p.ycrd())**2)

## @brief Rotates point around axis by phi (in radians)
#  @details Function takes in parameter phi as the rotation factor in terms of phi radians.
#  Current x and y coordinates of point are updated with below equations
#  @param phi is radians the point should be rotated by
    def rot(self, phi):
        self.xc = cos(phi) * self.xcrd() + (- sin(phi) * self.ycrd())
        self.yc = sin(phi) * self.xcrd() + cos(phi) * self.ycrd()
