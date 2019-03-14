'''
Created on 30 Oct 2017

@author: itoth
'''
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
from Utils import SearchForProperties
def test_add_number():
    assert AddNumber.add_number([12,13,13],1) == [12,13,13,1]
    assert AddNumber.add_number([],1) == [1]
    assert AddNumber.add_number([1,2,3,4,5],-100) == [1,2,3,4,5,-100]
    assert AddNumber.add_number([1,2,3],-1) == [1,2,3,-1]
    assert AddNumber.add_number([],0) == [0]
def test_insert_number():
    assert InsertNumberAtIndex.insert_number([1,2,3],-1,0) == [-1,2,3]
    assert InsertNumberAtIndex.insert_number([],4,3) == None
    assert InsertNumberAtIndex.insert_number([1,3],2,2) == None
    assert InsertNumberAtIndex.insert_number([1,4,5],1,2) == [1,4,1]
    assert InsertNumberAtIndex.insert_number([1,3,2],1,1) == [1,1,2]
def test_remove():
    assert RemoveIndex.remove([1,2,3],0) == [2,3]
    assert RemoveIndex.remove([],3) == None
    assert RemoveIndex.remove([2,3],1) == [2]
    assert RemoveIndex.remove([4,2,5],1) == [4,5]
    assert RemoveIndex.remove([1],0) == []
def test_remove_from_to():
    assert RemoveFromUntill.remove_from_to([1,2,3],1,2) == [1]
    assert RemoveFromUntill.remove_from_to([1],0,1) == []
    assert RemoveFromUntill.remove_from_to([1,2,3],0,2) == []
    assert RemoveFromUntill.remove_from_to([1,4,4,4],1,2) == [1,4]
    assert RemoveFromUntill.remove_from_to([1,3],4,1) == None
def test_replace():
    assert ReplaceSubarray.replace([1,2,3],[2],[2,3,4]) == [1,2,3,4,3]
    assert ReplaceSubarray.replace([],[],[1,2,3]) == None
    assert ReplaceSubarray.replace([],[1,2,3],[1,2,2,2,]) == None
    assert ReplaceSubarray.replace([1,2,3],[2,3],[1,2]) == [1,1,2]
    assert ReplaceSubarray.replace([1,4,4],[2,3],[1]) == [1,4,4]
def test_prime():
    assert SearchForProperties.prime(1) == False
    assert SearchForProperties.prime(4) == False
    assert SearchForProperties.prime(2) == True
    assert SearchForProperties.prime(144) == False
    assert SearchForProperties.prime(131) == True
def test_find_prime():
    assert FindPrime.find_prime([2,3,4],0,2) == [2,3]
    assert FindPrime.find_prime([],3,4) == None
    assert FindPrime.find_prime([1,2],4,1) == None
    assert FindPrime.find_prime([1,1,1,1,1],2,4) == []
    assert FindPrime.find_prime([2],0,0) == [2]
def test_find_odd():
    assert FindOdd.find_odd([2,3,4],0,2) == [3]
    assert FindOdd.find_odd([],3,4) == None
    assert FindOdd.find_odd([1,2],4,1) == None
    assert FindOdd.find_odd([1,1,1,1,1],2,4) == [1,1,1]
    assert FindOdd.find_odd([2],0,0) == []
def test_sum_from_till():
    assert SumFrom.sum_from_till([1,1,1,1],0,3) == 4
    assert SumFrom.sum_from_till([1,2],3,4) == None
    assert SumFrom.sum_from_till([1,3],1,0) == None
    assert SumFrom.sum_from_till([1,4,-4],1,2) == 0
    assert SumFrom.sum_from_till([444,1000,0],1,2) == 1000
def test_gcd():
    assert SearchForProperties.gcd(0,0) == 0
    assert SearchForProperties.gcd(0,10) == 10
    assert SearchForProperties.gcd(-1,10) == None
    assert SearchForProperties.gcd(2,4) == 2
    assert SearchForProperties.gcd(0,-1) == None
def test_find_gcd():
    assert GcdFrom.find_gcd([1,2],0,1) == 1
    assert GcdFrom.find_gcd([1,2,-1,4],1,3) == "No gcd found,we have negative numbers in there"
    assert GcdFrom.find_gcd([1,3,0,0,1],2,3) == 0
    assert GcdFrom.find_gcd([1,2,3,-1],0,2) == 1
    assert GcdFrom.find_gcd([],3,4) == None
def test_find_max():
    assert MaxFrom.find_max([1,3,2],0,3) == None
    assert MaxFrom.find_max([],1,3) == None
    assert MaxFrom.find_max([1,-1],4,5) == None
    assert MaxFrom.find_max([45,0,11,100],0,3) == 100
    assert MaxFrom.find_max([1,34,4,2,1],3,0) == None
def test_keep_prime():
    assert FilterPrime.keep_prime([1,3,10]) == [3]
    assert FilterPrime.keep_prime([4,4,2]) == [2]
    assert FilterPrime.keep_prime([]) == []
    assert FilterPrime.keep_prime([10,100]) == []
    assert FilterPrime.keep_prime([3,3,3]) == [3,3,3]
def test_keep_negative():
    assert FilterNegative.keep_negative([1,1,2,]) == []
    assert FilterNegative.keep_negative([-1,-1,3,4]) == [-1,-1]
    assert FilterNegative.keep_negative([]) == []
    assert FilterNegative.keep_negative([-1]) == [-1]
    assert FilterNegative.keep_negative([1]) == []
def verify():
    test_add_number()
    test_insert_number()
    test_remove()
    test_remove_from_to()
    test_replace()
    test_prime()
    test_find_prime()
    test_find_odd()
    test_sum_from_till()
    test_gcd()
    test_find_gcd()
    test_find_max()
    test_keep_prime()
    test_keep_negative()