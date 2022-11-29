"""
Definition: It is an efficient algorithm for sorting using divide-conquer approach.

Obs: It is slower compared with others sort algorithms, for small tasks.

Input:  sequence of n numbers <a1,a2,...,an>
Output: Permutation (reordering) <a1',a2',...,an'> where  a1'<a2'<...<an' for all cases.

Example:


input : [13,50,4,2,1,3]
expected output: [1,2,3,4,13,50]

PseudoCode:
    A = complete_items_list
    t = A.length //total items
    p = first_item_idx
    r = last_item_idx // t-1 
    q = middle_item_idx //  (t/2) - 1

    merge_sort(A,p,q,r)
        n1 = r-q

        // Left side   L = A[p,...,q] 
        // Right side  R = A[n1,...,r] 

        for i = p to q:
            L[i] = A[i]

        for j = n1 to r:
            R[j] = A[j]

        i = 0
        j = 0
        for k = p to r:
            if L[i] <= R[j]:
                A[k] = L[i]
                i = i+1
            else:
                A[K] = R[j]
                j = j + 1


Analysis
    divide = O(n)
    conquer = 2 * T/n2
    combine =  O(n)

    Best case:

    a1' < a2' < ... < an' 
    complexity O(n log(n))

    Worst case:

    a1' > a2' > ... > an'
    complexity O(n log(n))

Approach: Divide to conquer

"""
import typing


def divide_conquer(A: typing.Iterable[int]) -> typing.Iterable[int]:
    sequence_length = len(A)

    if sequence_length > 1:
        q = sequence_length // 2
        p = 0
        r = sequence_length
        merge_sort(A, q, r)

    return A


def merge_sort(A, q, r):
    L = A[:q]
    R = A[q:]

    if r == 1:
        return A

    else:
        L = merge_sort(L, len(L) // 2, len(L))
        R = merge_sort(R, len(R) // 2, len(R))

    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
        k += 1

    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1

    return A


"""
Usage:

    ipython3 or python3 (to access shell)

    from merge_sort import *

    items = [1,2,4,3,20,5]

    divide_conquer(items)

"""
