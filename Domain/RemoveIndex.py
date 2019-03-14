'''
Created on 30 Oct 2017

@author: itoth
'''
from Domain import GlobalVariable
from Domain import *
def remove(array,index):
    '''
    Input : the index of the element to be removed
    Output: A message telling us if the removing was succesfull
            we return the array if it was and we return None if it wasn't
    Restriction: The index MUST be smaller than the lenght
    '''
    GlobalVariable.previous_array = array[:]
    if index > len(array) - 1:
        return None
    del array[index]
    return array
