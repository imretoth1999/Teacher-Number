'''
Created on 30 Oct 2017

@author: itoth
'''
from Domain import GlobalVariable
from Domain import *
def find_max(array,begin,end):
    '''
    Input : the array we search,the index from where we begin and the index where we end our search
    Output: the max of the numbers from a given index till the other given index
    Restriction: begin MUST be smaller than end and end must be smaller than the length of the array. the array must not be empty
    '''
    GlobalVariable.previous_array = array[:]
    if begin > end or end >= len(array) or array == []:
        return None
    maximum = array[begin]
    for i in range(begin + 1,end):
        if max(array[i],array[i+1]) > maximum:
            maximum = max(array[i],array[i + 1])
    return maximum