## @file deque.py
#  @title deque
#  @author Meet Patel, patelm16
#  @date 2/27/2017

from circleADT import *

## @brief This class represents a deque of circle as an abstract object
#  @details A list, s, to store the CircleT objects and a constant, MAX_SIZE,
#  to help with the exceptions are globally created
class Deq:

    MAX_SIZE = 20

    s = []
    
## @brief Constructor which initializes deque s
    @staticmethod
    def init():
        Deq.s = []

## @brief Inserts a CircleT object into the back of the deque
#  @details The CircleT object is pushed assuming that the deque is not full;
#  if it is full, then an exception is raised
#  @param c is the CircleT object user wants to add to the back of the deque
    @staticmethod
    def pushBack(c):
        if len(Deq.s) == Deq.MAX_SIZE:
            raise FULL("Maximum size of deque is exceeded. Cannot add anymore circles.")
        else:
            Deq.s.append(c)

## @brief Inserts a CircleT object into the front of the deque
#  @details The CircleT object is pushed assuming that the deque is not full;
#  if it is full, then an exception is raised
#  @param c is the CircleT object user wants to add to the front of the deque
    @staticmethod
    def pushFront(c):
        if len(Deq.s) == Deq.MAX_SIZE:
            raise FULL("Maximum size of deque is exceeded. Cannot add anymore circles.")
        else:
            Deq.s = [c] + Deq.s

## @brief Removes a CircleT object from the back of the deque
#  @details The CircleT object is popped assuming that the deque is not empty already;
#  if it is empty, then an exception is raised
    @staticmethod
    def popBack():
        if len(Deq.s) == 0:
            raise EMPTY("The deque is empty; there is nothing to remove.")
        else:
            del Deq.s[-1]

## @brief Removes a CircleT object from the front of the deque
#  @details The CircleT object is popped assuming that the deque is not empty already;
#  if it is empty, then an exception is raised
    @staticmethod
    def popFront():
        if len(Deq.s) == 0:
            raise EMPTY("The deque is empty; there is nothing to remove.")
        else:
            del Deq.s[0]
            
## @brief Returns the CircleT object from the back of the deque
#  @details If deque is empty, then an exception is raised
#  @return the CircleT object from the back of the deque
    @staticmethod
    def back():
        if len(Deq.s) == 0:
            raise EMPTY("The deque is empty. There is nothing to return.")
        else:
            return Deq.s[-1]

## @brief Returns the CircleT object from the front of the deque
#  @details If deque is empty, then an exception is raised
#  @return the CircleT object from the front of the deque
    @staticmethod
    def front():
        if len(Deq.s) == 0:
            raise EMPTY("The deque is empty. There is nothing to return.")
        else:
            return Deq.s[0]

## @brief Returns the size of the deque
#  @return the length of the deque
    @staticmethod
    def size():
        return len(Deq.s)

## @brief Compares intersection between all CircleT objects in deque
#  @details If deque is empty, then an exception is raised. Additional if
#  statement included to account for when there is only one item in deque,
#  in which case, the assumption is that it does not intersect with any other
#  circles to provide a return value of true. For loops created in a way so that
#  an item is not compared to itself.
#  @return Boolean value returned; True if no circles in deque are intersecting
#  with any other; False returned if 1 or more intersections occur between 2 circles.
    @staticmethod
    def disjoint():
        if Deq.size() == 1:
            return True
        elif Deq.size() > 1:
            for i in Deq.s[:-1]:
                 for j in Deq.s[(Deq.s.index(i)+1):]:
                     if (i.intersect(j)):
                         return False
            return True
        else:
            raise EMPTY("The deque is empty. There are no circles to compare.")

## @brief Method calculates the sum of forces of the first item in deque with all
#  others in the deque.
#  @details If deque is empty, then an exception is raised. Division by zero
#  error is handled in local function, Fx() which is used to calculate force
#  between two CircleT objects using a function, f, provided by user. To account
#  for division by zero, an if statement is used.
#  @param f is the function inputted by user for which the force between two
#  CircleT objects is calculated with
#  @return the total sum of all forces between the first CircleT object with the others
    @staticmethod
    def sumFx(f):
        def __Fx__(f, ci, cj):
            if not (ci.connection(cj).len() == 0):
                return ci.force(f)(cj) * ((ci.cen().xcrd() - cj.cen().xcrd())/ci.connection(cj).len())
            else:
                return 0
        sumForces = 0              
        if len(Deq.s) == 0:
            raise EMPTY("The deque is empty. There are no circles to take the sum of.")
        else:
            for i in Deq.s[1:]:
                sumForces = sumForces + __Fx__(f,i,Deq.s[0])
            return sumForces


## @brief Function calculates total area of all CircleT objects in deque
#  @details If deque is empty, then an exception is raised.
#  @return Returns total sum of all areas of CircleT objects in deque
    @staticmethod
    def totalArea():
        if len(Deq.s) > 0:
            totalSum = 0
            for i in Deq.s:
                totalSum = i.area() + totalSum
            return totalSum
        else:
            raise EMPTY("The deque is empty. No area to calculate and find total of.")

## @brief Function calculates average radius of all CircleT objects in deque
#  @details If deque is empty, then an exception is raised.
#  @return Returns average radius of all radii of CircleT objects in deque
    @staticmethod
    def averageRadius():
        if len(Deq.s) > 0:
            sumRadii = 0
            for i in Deq.s:
                sumRadii = i.rad() + sumRadii
            return sumRadii/float(len(Deq.s))
        else:
            raise EMPTY ("The deque is empty. No radii to calculate and find average of.")

                                   
## @brief This is a class for when an exception is needed to be raised for when
#  the deque is full and a function is called to perform an operation on it                    
class FULL(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return str(self.value)

## @brief This is a class for when an exception is needed to be raised for when
#  the deque is empty and a function is called to perform an operation on it                      
class EMPTY(Exception):
  def __init__(self, ivalue):
    self.ivalue = ivalue
  def __str__(self):
    return str(self.ivalue)
