'''
Created on 30 Oct 2017

@author: itoth
'''
from Domain import FindPrime
from Domain import GlobalVariable
from Domain import *
def keep_prime(array):
    '''
    Input: the array from where we remove our non prime numbers
    Output: the array of prime numbers
    Restrictions: the array must not be empty
    '''
    GlobalVariable.previous_array = array[:]
    if array == []:
        return array
    return FindPrime.find_prime(array,0,len(array) - 1)