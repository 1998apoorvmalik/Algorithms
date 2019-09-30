"""
==========================================
Title:  Binary Search
Author: Apoorv Malik
Date:   30 September, 2019
==========================================
"""

import random

# Specify the parameters for the array.
SIZE = 20
LOW = -100
HIGH = 100

def generateRandomArray(size, low, high):   # Utility function to generate random array of fixed size in range low -> high.
    return [random.randint(low, high) for _ in range(size)]

def mergeSort(array):
    if len(array) > 1:                      # Ensure that the length of array is greater than one.
        mid = len(array) // 2               # Finding the middle index of the array.
        # Dividing the array into two halves.
        L = array[:mid]                     # Left half of the array
        R = array[mid:]                     # Right half of the array

        mergeSort(L)                        # Sorting the first half of the array
        mergeSort(R)                        # Sorting the second half of the array

        i = j = k = 0

        while i < len(L) and j < len(R):    # Combining the L and R arrays and copying the data from them.
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):                   # Ensuring that no element is leftto copy from the L array.
            array[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):                   # Ensuring that no element is left to copy from the R array.
            array[k] = R[j]
            j += 1
            k += 1
    
    return array

def printArray(array):                      # Utility function to print an array.
    for i in array:
        print(i, end = ' ')

# Generating a random array.
array = generateRandomArray(SIZE, LOW, HIGH)

# Printing the unsorted array.
print("\nUnsorted array is :")
printArray(array)
print("\n\n")

# Sorting the random array using merge sort.
array = mergeSort(array)

# Printing the sorted array.
print("Sorted array is :")
printArray(array)
print("\n\n")