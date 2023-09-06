#!/usr/bin/env python3

def bubbleSort(array):
    n = len(array)
    swapped = False
    for i in range(0, n):
        for j in range(0, n - i -1):
            if array[j] > array[j+1]:
                swapped = True
                array[j], array[j+1] =  array[j+1], array[j]
        
        # an optimization could be if after first loop iteration of j
        # no swap has occoured, means the array is already sorted, jsut return
        # no need to perform any more processing
        if not swapped:
            return
            



arr4 = [-2, 45, 0, 11, -9,88,-97,-202,747]

if __name__ == "__main__":
    print("BUBBLESORT  - o(n^2 WORST)")

    print(f"Unsorted: {arr4}")
    bubbleSort(arr4)
    print(f"Sorted: {arr4}")
    
    # case when alrady sorted: best case
    arr5 = [0, 1, 2, 3, 4, 6]

    print(f"Unsorted2: {arr5}")
    bubbleSort(arr5)
    print(f"Sorted2: {arr5}")


"""
TC: O(n^2) :  worst, avg, 
best: O(n)
SC: O(1): In place
Stable algo
"""