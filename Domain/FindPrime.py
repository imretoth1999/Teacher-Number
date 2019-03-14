'''
Created on 30 Oct 2017

@author: itoth
'''
from Domain import GlobalVariable
from Domain import *
from Utils import SearchForProperties
def find_prime(array,begin,end):
    '''
    Input: the array we search, the index where we begin and the index where we end our search
    Output: an array containing all the prime numbers found
    Restrictions: begin MUST be smaller than end and end MUST be smaller than the lenght of the array. the array MUST not be empty
    '''
    GlobalVariable.previous_array = array[:]
    if begin > end or end >= len(array) or array == []:
        return None
    found = []
    for i in range(begin,end+1):
        if SearchForProperties.prime(array[i]) == True:
            found.append(array[i])
    return found