'''
Created on 30 Oct 2017

@author: itoth
'''
import itertools
from Domain import GlobalVariable
from Domain import *
def find_subarray(array, subarray):
    '''
    Input: The array and the subarray we want to find
    Output: The beginning and end indexes of the subarray in the given array
    Restruction: none
    '''
    length = len(subarray)
    for index, value in enumerate(array):
        if value == subarray[0] and array[index:index+length] == subarray:
            yield index, index+length
def replace(array, target, replacement, maxreplace=None):
    '''
    Input: The array we want to modify, the target and replacement of the target
    Output: The array with the target subarray changed to the replacement subarray
    Restriction: The given array MUST not be empty
    '''
    GlobalVariable.previous_array = array[:]
    sublists = find_subarray(array, target)
    if array == []:
        return None
    if maxreplace:
        sublists = itertools.islice(sublists, maxreplace)
    for start, end in sublists:
        array[start:end] = replacement
    return array