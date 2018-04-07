import pyximport
pyximport.install(pyimport=True)

import time
import json
import sys
import os

from utils import create_rand_array
from cocktailsort import cocktail_sort
from heapsort import heap_sort
from quicksort import quick_sort

sys.setrecursionlimit(4000)


def sort_array(array, array_size, method='quick'):
    if method == 'quick':
        quick_sort(array, 0, array_size - 1)
    elif method == 'heap':
        heap_sort(array)
    elif method == 'cocktail':
        cocktail_sort(array)


if __name__ == '__main__':
    methods = ['quick', 'heap', 'cocktail']
    times = {x: {} for x in methods}
    array_sizes = range(10000, 100001, 5000)
    for arr_size in array_sizes:
        print(f'Testing for {arr_size} elements')
        for method in methods:
            try:
                arr = create_rand_array(arr_size)
                start_time = time.time()
                sort_array(arr, arr_size, method)
                end_time = time.time()
                exec_time = round(end_time - start_time, 5)
                times[method][arr_size] = exec_time
            except RecursionError:
                times[method][arr_size] = float('nan')
    with open('sorting_times.json', 'w') as json_file:
        json.dump(times, json_file, indent=4, ensure_ascii=False)