'''
Created on 30 Oct 2017

@author: itoth
'''
from UI import UserInput
def create_array():
    n = UserInput.user_input()
    i = 0
    array = []
    while i != n:
        array.append(UserInput.user_input())
        i += 1
    return array