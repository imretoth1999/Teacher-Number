'''
Created on 30 Oct 2017

@author: itoth
'''
from Domain import GlobalVariable
from Domain import *
def undo_operation():
    array = GlobalVariable.previous_array[:]
    return array