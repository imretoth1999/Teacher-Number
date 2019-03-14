'''
Created on 30 Oct 2017

@author: itoth
'''
from Domain import GlobalVariable
from Domain import *
def add_number(array,a):
    '''
    Input : the number to be added to the array
    Output: A message telling us if the adding was succesfull
            we return the array if it was and we return None if it wasn't
    Restriction: The variable given can only be a number
    '''
    GlobalVariable.previous_array = array[:]
    array.append(a)
    return array