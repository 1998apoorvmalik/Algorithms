"""
==========================================
Title:  Binary Search
Author: Apoorv Malik
Date:   30 September, 2019
==========================================
"""

# Imports
import random

# Specify the parameters for the array.
SIZE = 20
LOW = -100
HIGH = 100
ELEMENT = 34

# Utility function to generate random sorted array of fixed size in range low -> high. Also, include element 
# in the array if element argument is not None.
def generateRandomSortedArray(size, low, high, element=None): 
    temp = [random.randint(low, high) for _ in range(size)]
    if element != None:
        temp.append(element)
    temp = list(set(temp))
    temp.sort()
    return temp

def printArray(array):                      # Utility function to print an array.
    for i in array:
        print(i, end = ' ')
    print("\n")

# Python Program for recursive binary search. Function will return the index of the element in the array, if present, 
# else it will return -1.

def binarySearchRecursive(array, element, l, r):
    # Check base case,
    if r >= l:
        
        # Define the middle index of the array.
        mid = l + (r - l)/2
        mid = int(mid)  # Converting to int.

        # If element is present at the middle itself, then return mid index.
        if array[mid] == element:
            return mid
        
        elif array[mid] > element:  # The element is not present in the right subarray, search in the left subarray.
            return binarySearchRecursive(array, element, l, mid-1,)
        
        else:   # The element is not present in the left subarray, search in the right subarray.
            return binarySearchRecursive(array, element, mid+1, r)
    
    else:
        # Element is not present in the array.
        return -1

# Python Program for iterative binary search. Function will return the index of the element in the array, if present, 
# else it will return -1.
def binarySearchIterative(array, element):
    l = 0
    r = len(array) - 1

    while l <= r:

        # Define the middle index of the array.
        mid = l + (r - l)/2
        mid = int(mid)  # Converting to int.

        # If element is present at the middle itself, then return mid index.
        if array[mid] == element:
            return mid
        
        elif array[mid] > element:  # The element is not present in the right subarray, search in the left subarray.
            r = mid - 1
        
        else:   # The element is not present in the left subarray, search in the right subarray.
            l = mid + 1
    
    # Element is not present in the array.
    return -1

# Driver code to test the above code.
if __name__ == '__main__': 
    # Generating a random sorted array.
    array = generateRandomSortedArray(SIZE, LOW, HIGH, ELEMENT)

    # Printing the sorted array.
    print("Sorted array is :")
    printArray(array)

    # Finding the index of the element in the array using recursive binary search.
    print("Searching element '{}' using Recursive Binary Search:".format(ELEMENT))
    index = binarySearchRecursive(array, ELEMENT, 0, len(array)-1)
    if index != -1:
        print("The element is found at index: ", index)
    else:
        print("The element is not present in the array")
    
    print("\n")     # Extra space

    # Finding the index of the element in the array using iterative binary search.
    print("Searching element '{}' using Iterative Binary Search:".format(ELEMENT))
    index = binarySearchIterative(array, ELEMENT)
    if index != -1:
        print("The element is found at index: ", index)
    else:
        print("The element is not present in the array")
    
    print("\n")     # Extra space