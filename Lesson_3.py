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

# Testing

input = [4, 2, 6, 3, 4, 6, 2, 1]
output = insertion_sort(input)


print("Input: {}".format(input))
print("Output: {}".format(output))
