
## Sorting Algorithms

<hr>

### Insertion Sort

**Definition**: It is an efficient algorithm for sorting small number of elements.

Input:  sequence of n numbers **<a1,a2,...,an>**

Output: Permutation (reordering) **<a1',a2',...,an'>** where  **a1'<a2'<...<an'** for all cases.

**Example**:

input : [13,50,4,2,1,3,33]

expected output: [1,2,3,4,13,33,50]

**PseudoCode**:

    for j=1 to input.length
        current_value = input[j]
        before_index = j - 1
        
        while before_index >= 0 and input[before_idx] > current_value
            input[before_index+1] = input[before_idx]
            before_index = before_index -1
        input[before_index+1] = current_value


**Analysis**

    Best case:

    a1' < a2' < ... < an' 
    complexity O(n)

    Worst case:

    a1' > a2' > ... > an'
    complexity O(n²)

**Approach**: Incremental

<hr>

### Merge sort

**Definition**: It is an efficient algorithm for sorting using divide-conquer approach.

Input:  sequence of n numbers <a1,a2,...,an>

Output: Permutation (reordering) <a1',a2',...,an'> where  a1'<a2'<...<an' for all cases.

**Example**:

input : [13,50,4,2,1,3]

expected output: [1,2,3,4,13,50]

**PseudoCode**:
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


**Analysis**
    divide = O(n)
    conquer = 2 * T/n2
    combine =  O(n)

    Best case:

    a1' < a2' < ... < an' 
    complexity O(n log(n))

    Worst case:

    a1' > a2' > ... > an'
    complexity O(n log(n))

**Approach**: Divide to conquer


<hr>

### References

- H.Cormem,Thomas - Introduction to Algorithms , third edition