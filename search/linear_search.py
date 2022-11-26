"""
Definition: It scans  through the sentence looking for value existence into  items list.

Input:  sequence of n numbers input = <a1,a2,...,an> and needed value v
Output: An index i if v = input[i] or None case v don't exists in input

Examples:

input : [13,50,4,2,1,3,33] , 13
expected output: 0


input : [13,50,4,2,1,3,33] , 55
expected output: None

PseudoCode:

    need_value = v
    finded_index = None
    for j=0 to input.length
        current_value = input[j]

        if current value == v:
            finded_index = j
            break
    
    return findex_index
    
"""

import typing


def linear_search(items: typing.Iterable[int], value: int) -> typing.Union[int, None]:

    finded_index = None

    for idx, current_value in enumerate(items):
        if current_value == value:
            finded_index = idx
            break

    return finded_index


"""
Usage:

from linear_search import *

items = [1,2,3,4]

value = 2

linear_search(items,value)

"""
