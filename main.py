import pyximport
pyximport.install(pyimport=True)

from cocktailsort import cocktail_sort
from heapsort import heap_sort
from quicksort import quick_sort

if __name__ == '__main__':
    arr = [5, 1, 4, 2, 8, 0, 2]
    n = len(arr)
    heap_sort(arr)
    cocktail_sort(arr)
    quick_sort(arr, 0, n - 1)
    print("Sorted array is")
    for i in arr:
        print("%d" % i)