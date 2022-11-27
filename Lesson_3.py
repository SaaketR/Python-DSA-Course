'''
Lesson 3 - Merge Sort, Quick Sort, and Divide and Conquer Algortihm

Question:
    You are working on a new feature on Jovian called "Top Notebooks of the Week". rite a function to sort a list of notebooks 
    in decreasing order of likes. Keep in mind that up to millions of notebooks can be created every wweek, so your code has to be
    efficiently as possible.

Interpretation of the Question:
    Write a program to sort a list of number in decreasing order.

Test Cases:
    1. [4, 2, 6, 3, 4, 6, 2, 1] (random order)
    2. [5, 2, 6, 1, 23, 7, -12, 12, -243, 0] (random order)
    3. [3, 5, 6, 8, 9, 10, 99] (already sorted)
    4. [99, 10, 9, 8, 6, 5, 3] (already sorted, in decreasing order)
    5. [5, -12, 2, 6, 1, 23, 7, 7, -12, 6, 12, 1, -243, 1, 0] (contains repeating elements)
    6. [] (empty list)
    7. [23] (list containing only one elemet)
    8. [21,21,21,21,21] (list containing one element repeated multiple times)

Bubble Sort Algorithm:
    1. Iterate over the array
    2. Compare the current element with the number that follows it
    3. If the following number is greater (or smaller, in case of ascending order) swap the two elements
    4. Repeat, until array is sorted

Insertion Sort Algorithm (source: https://www.geeksforgeeks.org/insertion-sort/)
    1. Iterate over the array, starting from the second element
    2. Compare the current element (key) with the preceeding elements
    3. If the key element is greater (or smaller, in case of ascending order), swap the two elements, and repeat until the key is 
    at the correct position
    4. Repeat, until the array is sorted

Divide and Conquer:
    1. Divide array into two equal parts
    2. Recursively solve the problem for each of the two parts
    3. Combine the results to solve the problem
    4. Inlcude terminating conditions for small and indivisible inputs

Merge Sort (Divide and Conquer):
    1. Find the middle index and divide the array into its left half and right half (until the lengths are atomically divisible)
    2. Perform the merge sort for the left half and right half respectively
    3. Merge the sorted arrays by comparing the elements in the left and right half and placing them the appropriate order
'''

# Bubble Sort, descending order [Time = O(N^2); Space = O(N)]

def bubble_sort(array):
    arr = list(array)     # creating a copy of the array to not directly change the input array

    i = 0
    while (i < len(arr)-1):     # repeating the process n-1 times, where n is the length of the array
        j = 0
        while (j < len(arr)-1):     # performing the bubble sort
            if (arr[j+1] > arr[j]):     # comparing and arranging in descending order
                arr[j], arr[j+1] = arr[j+1], arr[j]         # swapping the numbers
            j += 1
        i += 1
    
    return arr

# Insertion Sort, descending order [Time = O(N^2); Space = O(1)]

def insertion_sort(array):
    arr = list(array)       # creating a copy of the array to not directly change the input array

    i = 1
    while (i < len(arr)):       # iterating over the input array
        key = arr[i]        # storing the current element into a variable (key)
        
        j = i-1
        while ((j >= 0) and (key > arr[j])):        # conditions to find the appropriate position for the key
            arr[j+1] = arr[j]       # pushing the preceeding element forward (swapping)
            j -= 1
        arr[j+1] = key      # appropriate position found, insert the key here

        i += 1
    return arr

# Merge Sort, ascending order [Time = O(N log(N)); Space = O(N)]

def merge_sort(array):
    if (len(array) <= 1):       # Condition for when the input is empty or contains just one element
        return array

    sorted = []     # Creating a separate array for the sorted result to avoid directly altering the input array
    
    # Declaring the middle index, hence dividing the array into its left and right halves
    mid = len(array) // 2
    L, R = array[:mid], array[mid:]

    # Performing the merge sort function on the left and right halves respectively
    L, R = merge_sort(L), merge_sort(R)
    
    # Perfoming the Merging function
    i, j = 0, 0
    while (i < len(L) and j < len(R)):      # Iterating through the halves, comparing their elements, and placing them in the appropriate order
        if (L[i] <= R[j]):
            sorted.append(L[i])
            i += 1
        else:
            sorted.append(R[j])
            j += 1
    
    # Identifying any element that may have been left out during the Merging function
    while (i < len(L)):
        sorted.append(L[i])
        i += 1
    
    while (j < len(R)):
        sorted.append(R[j])
        j += 1
    
    return sorted

# Testing

input = [99, 10, 9, 8, 6, 5, 3]
output = merge_sort(input)


print("Input: {}".format(input))
print("Output: {}".format(output))
