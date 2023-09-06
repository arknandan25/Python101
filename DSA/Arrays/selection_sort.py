#!/usr/bin/env python3

def selectionSort(array):
    # breakpoint()
    for i in range(0, len(array)):
        smallest = array[i]
        pos_of_smallest_element = i
        for j in range(i+1, len(array)):
            if array[j] < smallest:
                smallest = array[j]
                pos_of_smallest_element = j
        array[i], array[pos_of_smallest_element] = array[pos_of_smallest_element], array[i]


arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
arr2 = [0, 1, 2, 3, 4, 6, 0]
if __name__ == "__main__":
    selectionSort(arr)
    print(f"Unsorted: {arr}")
    print(f"Sorted: {arr}")
    selectionSort(arr2)
    print(f"Unsorted2: {arr2}")
    print(f"Sorted2: {arr2}")


"""
TC: O(n^2) :  worst, avg, best
SC: O(1): In place
Stable algo
"""