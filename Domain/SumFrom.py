'''
Created on 30 Oct 2017

@author: itoth
'''
from Domain import GlobalVariable
from Domain import *
def sum_from_till(array,begin,end):
    '''
    Input: the array we search, the index from where we begin and the index  where we end our calculation
    Output: the sum of the numbers from a given index till the other given index
    Restrictions: begin MUST be smaller than end and end must be smaller than the length of the array. the array must not be empty
    '''
    GlobalVariable.previous_array = array[:]
    if begin > end or end >= len(array) or array == []:
        return None
    s = 0
    for i in range(begin,end + 1):
        s += array[i]
    return s