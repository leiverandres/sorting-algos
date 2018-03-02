def cocktail_sort(array):
    cdef int start, end, n
    n = len(array)
    swapped = True
    start = 0
    end = n - 1
    while (swapped == True):
        swapped = False

        # loop from left to right
        for i in range(start, end):
            if (array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        # if nothing moved, then array is sorted.
        if (swapped == False):
            break

        # otherwise, reset the swapped flag so that it
        # can be used in the next stage
        swapped = False
        end = end - 1

        # from right to left
        for i in range(end - 1, start - 1, -1):
            if (array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        start = start + 1

