
## Sorting Algorithms

### Insertion Sort

Definition: It is an efficient algorithm for sorting small number of elements.

Input:  sequence of n numbers **<a1,a2,...,an>**
Output: Permutation (reordering) **<a1',a2',...,an'>** where  **a1'<a2'<...<an'** for all cases.

Example:

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


### References

- H.Cormem,Thomas - Introduction to Algorithms , third edition