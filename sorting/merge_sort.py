"""
Definition: It is an efficient algorithm for sorting using divide-conquer approach.

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

    Best case:

    a1' < a2' < ... < an' 
    complexity O(n)

    Worst case:

    a1' > a2' > ... > an'
    complexity O(n²)

Approach: Divide to conquer

"""


def merge_sort(A, p, q, r):
    n1 = r - q
    L = A[p:q]
    R = A[n1:r]

    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

