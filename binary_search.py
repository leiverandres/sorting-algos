import pyximport
pyximport.install(pyimport=True)
from random import randint
import time
import json

from utils import create_rand_array


def binary_search(arr, query):
    low = -1  # arr[low] <= query
    high = len(arr)  # arr[high] > query
    while high - low > 1:
        mid = (high + low) // 2
        if arr[mid] <= query:
            low = mid
        else:
            high = mid
    if arr[low] == query:
        return low
    else:
        return -1


def recursive_binary_search(arr, query, low, high):
    mid = (high + low) // 2
    if low > high:
        return -1
    elif arr[mid] == query:
        return mid
    elif arr[mid] > query:
        return recursive_binary_search(arr, query, low, mid - 1)
    else:
        return recursive_binary_search(arr, query, mid + 1, high)


def linear_search(arr, query):
    for i, num in enumerate(arr):
        if num == query:
            return i
    return -1


def find(arr, query, method='binary_search'):
    idx = -1
    if method == 'binary_search':
        idx = binary_search(arr, query)
    elif method == 'linear':
        idx = linear_search(arr, query)
    return idx


if __name__ == '__main__':
    methods = ['linear', 'binary_search']
    # array_sizes = [10**x for x in range(1, 9)]
    array_sizes = range(100000, 1000001, 50000)
    run_times = 10
    times = {x: {} for x in methods}
    for arr_size in array_sizes:
        arr = create_rand_array(arr_size)
        arr_sorted = sorted(arr)
        query = -1
        for method in methods:
            acum_time = 0
            for i in range(run_times):
                start_time = time.time()
                if method == 'binary_search':
                    idx = find(arr_sorted, query, method)
                else:
                    idx = find(arr, query, method)
                end_time = time.time()
                acum = round(end_time - start_time, 10)
            times[method][arr_size] = acum / run_times
    with open('searching_times.json', 'w') as json_file:
        json.dump(times, json_file, indent=4, ensure_ascii=False)