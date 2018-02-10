## @file Statistics.py
#  @title Statistics
#  @author Meet Patel
#  @date 1/28/2017

import numpy 
import CircleADT

## @brief Calculates the average radius from a given list of circle objects
#  @details Uses numpy library to calculate the average.
#  @param List containing circles created by CircleT class.
#  @return Average radius of the list of circles.
def average(circles):
    radiiList = [ i.radius() for i in circles]
    return numpy.average(radiiList) 

## @brief Calculates the standard deviation of the radii from a given list of circle objects
#  @details Uses numpy library to calculate the standard deviation.
#  @param List containing circles created by CircleT class.
#  @return Standard deviation of the radii of the list of circle objects.
def stdDev(circles):
    radiiList = [i.radius() for i in circles]
    return numpy.std(radiiList)

## @brief Creates a list of the ranking of the radii from a given list of circle objects in descending order.
#  @details Assumed that the ranking when two or more elements are the same
#  is produced by that rank appearing the same number of times and the next number being skipped
#  ie; rank of radii [9,4,6,2,4] would be [1,3,2,5,3] (notice there is nothing ranked as 4)
#  @param List containing circles created by CircleT class.
#  @return List ranked by descending order of radii of list of circle objects
def rank(circles):
    
    radiiList = []
    
    for i in circles:
        radiiList.append(i.radius())
        
    sortedList = sorted(radiiList, reverse=True)
    rankedList = []
    
    for i in radiiList:
        rankedList.append(sortedList.index(i)+1)
        
    return rankedList
