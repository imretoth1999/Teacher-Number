'''
Created on 30 Oct 2017

Content: This module contains every function used in helping the user
use the program. This means it contains everything related to the menu
and the user input.

@author: itoth
'''
from Domain import CreateArray
from Domain import AddNumber
from Domain import FilterNegative
from Domain import FilterPrime
from Domain import FindOdd
from Domain import FindPrime
from Domain import GcdFrom
from Domain import InsertNumberAtIndex
from Domain import MaxFrom
from Domain import RemoveFromUntill
from Domain import RemoveIndex
from Domain import ReplaceSubarray
from Domain import SumFrom
from Domain import GlobalVariable
from Domain import Undo
from UI import UserInput
def menu():
    '''
    Input: the number of the elements and the elements.
            After that we have request the number of the function and the inputs neccesary for the function
    Output: The array modified
    Restrictions: None
    '''
    a = -2
    print("Hello students! Welcome to the program!")
    array = CreateArray.create_array()
    print("Now that you created your array you can play with it")
    print(".....................................................")
    GlobalVariable.previous_array = array[:]
    while a != 0:
        print("Input -2 for creating another array")
        print("Input -1 for viewing your array")
        print("Input 0 for exiting the program")
        print("Input 1 for adding an element to the end of the array")
        print("Input 2 for inserting an element at a given index")
        print("Input 3 for removing an element at a given index")
        print("Input 4 for removing the elements from a given index till another given index")
        print("Input 5 for replacing a subarray with another subarray")
        print("Input 6 for finding all the prime numbers from a given index till another given index")
        print("Input 7 for finding all the odd numbers from a given index till another given index")
        print("Input 8 for calculating the sum of the numbers in the array from a given index till another given index")
        print("Input 9 for finding the gcd of the numbers in the array from a given index till another given index")
        print("Input 10 for finding the max of the numbers in the array from a given index till another given index")
        print("Input 11 for keeping only prime numbers")
        print("Input 12 for keeping only negative numbers")
        print("Input 13 for undoing the last operation")
        print(".....................................................")
        a = UserInput.user_input()
        if a == -1:
            print(".....................................................")
            print("The array you now have is ",end = ' ')
            print(array)
            print(".....................................................")
        elif a == -2:
            array = CreateArray.create_array()
            print("The array has been created")
            print(".....................................................")
            print("The array you now have is ",end = ' ')
            print(array)
            print(".....................................................")
        elif a == 1:
            print(".....................................................")
            print("You requested to use the adding function")
            AddNumber.add_number(array,UserInput.user_input())
            print(".....................................................")
            print("The array you now have is: ",end = ' ')
            print(array)
            print(".....................................................")
        elif a == 2:
            print(".....................................................")
            print("You have requested to use the inserting function")
            InsertNumberAtIndex.insert_number(array,UserInput.user_input(),UserInput.user_input())
            print(".....................................................")
            print("The array you now have is ",end = ' ')
            print(array)
            print(".....................................................")
        elif a == 3:
            print(".....................................................")
            print("You have requested to use the removing and element at the index function")
            RemoveIndex.remove(array,UserInput.user_input())
            print(".....................................................")
            print("The array you now have is ",end = ' ')
            print(array)
            print(".....................................................")
        elif a == 4:
            print(".....................................................")
            print("You have requested to use the removing and elements from a given begin and end")
            RemoveFromUntill.remove_from_to(array,UserInput.user_input(),UserInput.user_input())
            print(".....................................................")
            print("The array you now have is ",end = ' ')
            print(array)
            print(".....................................................")
        elif a == 5:
            print(".....................................................")
            print("You have requested to replace a subarray with another subarray")
            ReplaceSubarray.replace(array,CreateArray.create_array(),CreateArray.create_array())
            print(".....................................................")
            print("The array you now have is ",end = ' ')
            print(array)
            print(".....................................................")
        elif a == 6:
            print(".....................................................")
            print("You have requested to find all the prime numbers from a given index till another")
            primes = FindPrime.find_prime(array,UserInput.user_input(),UserInput.user_input())
            print(".....................................................")
            print("The prime numbers from the given index till the other are : ",end = ' ')
            print(primes)
            print(".....................................................")
        elif a == 7:
            print(".....................................................")
            print("You have requested to find all the odd numbers from a given index till another")
            odd = FindOdd.find_odd(array,UserInput.user_input(),UserInput.user_input())
            print(".....................................................")
            print("The odd numbers from the given index till the other are : ",end = ' ')
            print(odd)
            print(".....................................................")
        elif a == 8:
            print(".....................................................")
            print("You have requested to calculate the sum of all numbers from a given index till another")
            s = SumFrom.sum_from_till(array,UserInput.user_input(),UserInput.user_input())
            print(".....................................................")
            print("The sum is ",end = ' ')
            print(s)
            print(".....................................................")
        elif a == 9:
            print(".....................................................")
            print("You have requested to find the gcd of all numbers from a given index till another")
            s = GcdFrom.find_gcd(array,UserInput.user_input(),UserInput.user_input())
            print(".....................................................")
            print("The gcd is : ",end = ' ')
            print(s)
            print(".....................................................")
        elif a == 10:
            print(".....................................................")
            print("You have requested to find the max of all numbers from a given index till another")
            s = MaxFrom.find_max(array,UserInput.user_input(),UserInput.user_input())
            print(".....................................................")
            print("The max is : ",end = ' ')
            print(s)
            print(".....................................................")
        elif a == 11:
            print(".....................................................")
            print("You have requested to keep only the prime numbers")
            array = FilterPrime.keep_prime(array)
            print(".....................................................")
            print("The array you now have is : ",end = ' ')
            print(array)
            print(".....................................................")
        elif a == 12:
            print(".....................................................")
            print("You have requested to keep only the negative numbers")
            array = FilterNegative.keep_negative(array)
            print(".....................................................")
            print("The array you now have is : ",end = ' ')
            print(array)
            print(".....................................................")
        elif a == 13:
            print(".....................................................")
            print("You have requested to undo the last operation")
            array = Undo.undo_operation()
            print(".....................................................")
            print("The array you now have is : ",end = ' ')
            print(array)
            print(".....................................................")
        elif a != -2 and a != 0 and a != 1 and a != 2 and a != -1 and a != 3 and a != 4 and a != 5 and a != 6 and a != 7 and a != 8 and a != 9 and a != 10 and a != 11 and a != 12 and a != 13:
            print(".....................................................")
            print("Enter an existing function number please")
            print(".....................................................")