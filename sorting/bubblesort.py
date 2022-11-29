"""
Definition: It is an efficient algorithm for sorting small number of elements.

Obs: It's useful for smaller sets of elements but is inefficient for larger sets

Input:  sequence of n numbers <a1,a2,...,an>
Output: Permutation (reordering) <a1',a2',...,an'> where  a1'<a2'<...<an' for all cases.

Example:


input : [13,50,4,2,1,3]
expected output: [1,2,3,4,13,50]

PseudoCode:
    
    A = complete_item_list
    bubble_sort(A)
        for i = 0 to A.length -1
            for j= A.length downto i + 1
                if A[j] < A[j-1]
                    exchange A[j] with A[j-1]


Analysis
   
    Best case:
    a1' < a2' < ... < an' 
    complexity O(n)

    Worst case:
    a1' > a2' > ... > an'
    complexity  0(n²)

Approach: Incremental

"""


def bubble_sort(A):
    for i in range(0, len(A)):
        for j in range(len(A) - 1, i, -1):
            if A[j] < A[j - 1]:
                to_exchange = A[j]
                A[j] = A[j - 1]
                A[j - 1] = to_exchange
    return A


bubble_sort([3, 5, 2, 1, 0, -1])
bubble_sort([6, 5, 4, 3, 2, 1])

