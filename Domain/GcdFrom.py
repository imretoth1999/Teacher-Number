'''
Created on 30 Oct 2017

@author: itoth
'''
from Domain import GlobalVariable
from Domain import *
from Utils import SearchForProperties
def find_gcd(array,begin,end):
    '''
    Input : the array we search,the index from where we begin and the index where we end our search
    Output: the gcd of the numbers from a given index till the other given index
    Restriction: begin MUST be smaller than end and end must be smaller than the length of the array. the array must not be empty
    '''
    GlobalVariable.previous_array = array[:]
    if begin > end or end >= len(array) or array == []:
        return None
    gcd_value = 0
    for i in range(begin,end):
        gcd_value = SearchForProperties.gcd(array[i],array[i + 1])
        if gcd_value == None:
            return "No gcd found,we have negative numbers in there"
    return gcd_value