'''
Created on 30 Oct 2017

@author: itoth

This module contains every function that helps us to find a property for a number
'''
import math

def gcd(a, b):
    '''
    Input: 2 natural numbers
    Output: the greatest common divisor of those 2 numbers
    Restriction: the numbers must be natural numbers
    '''
    if a < 0 or b < 0:
        return None
    elif (a == 0):
        if (b == 0):
            return 0
        else:
            return b
    else:
        if (b == 0):
            return a
        else:
            while (a != b):
                if (a > b):
                    a = a - b
                else:
                    b = b - a
            return a

def prime(n):
    '''
We create another function that returns true if n is prime or false if it's not
First we exclude the cases where n is an even number and it's not 2 and the
cases where n is 0 or 1
If n is 2 then we return true because 2 is the only even prime number
After that we go to the square root of n and we verify if it has any divisors
If it has we return False and if it doesn't have we return True
INPUT: the number we verify if it's prime or not
OUTPUT: the statement if the number is prime or not

    '''
    if (n % 2 == 0 and n != 2) or n == 1 or n == 0:
        return False
    elif n == 2:
        return True
    else:
        for d in range(3, int(math.sqrt(n)) + 1, 2):
            if n % d == 0:
                return False
        return True