'''
Created on 30 Oct 2017

@author: itoth
'''
from Domain import GlobalVariable
from Domain import *
def remove_from_to(array,begin,end):
    '''Input: the array the begining and the end. we delete from begin until the end
        Output: the array modified
        Restriction : begin must be smaller than end and end must be smaller than the lenght of the array
    '''
    GlobalVariable.previous_array = array[:]
    if begin > end or end > len(array):
        return None
    del array[begin:end+1]
    return array