'''
Created on 30 Oct 2017

@author: itoth
'''
from Domain import GlobalVariable
from Domain import *
def keep_negative(array):
    '''
    Input: the array from where we remove our non negative numbers
    Output: the array of negative numbers
    Restrictions: the array must not be empty
    '''
    GlobalVariable.previous_array = array[:]
    if array == []:
        return array
    negative = []
    for elem in array:
        if elem < 0:
            negative.append(elem)
    return negative