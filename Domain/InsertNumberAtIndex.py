'''
Created on 30 Oct 2017

@author: itoth
'''
from Domain import GlobalVariable
from Domain import *
def insert_number(array,n,index):
    '''
    Input: the array, the number and the index to which the number will be placed
    Output: the array with the requested number on the specific index.
    Restriction: the index MUST be smaller than the lenght
    '''
    GlobalVariable.previous_array = array[:]
    if index > len(array) - 1:
        return None
    array[index] = n
    return array