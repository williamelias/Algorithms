import time

from insertion_sort import increasing_insertion_sort
from merge_sort import divide_conquer, merge_sort

best_case = [1, 2, 3, 4, 5]

import random

# randomlist = []
# for i in range(0, 20000000):
#     n = random.randint(1, 20000000)
#     randomlist.append(n)
# worst_case = randomlist


def merge_sort_time(worst_case):
    len_worst_case = len(worst_case)
    q = len_worst_case // 2

    start = time.time()
    merge_sort(worst_case, q, len_worst_case)

    return time.time() - start


def insertion_sort_time(worst_case):

    start = time.time()
    increasing_insertion_sort(worst_case)

    return time.time() - start


def run():

    print('___Running worst case__')

    print(f'merge_sort time : {merge_sort_time()}')

    print(f'insertion_sort time: {insertion_sort_time()}')

