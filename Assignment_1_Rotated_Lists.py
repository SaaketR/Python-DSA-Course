'''
Assignment 1 - Rotated Lists Using Binary Search

Overview:
    This file covers Assignment 1 of the Python DSA course by Jovian.ai. To maintain academic integrety, the entire assignment 
    notebook will not be posted here. Instead, only code relevant to the concept of rotated lists will be written below. 
    Since the assignment also asks for a list of test cases, I will not be listing the test cases I use.

Problem Statement:
    Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. 
    Your function should have the worst-case complexity of O(log N), where N is the length of the list. You can assume that 
    all the numbers in the list are unique.

    Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.

Linear Search Solution Explanation:
    The number of rotations can be obtained by finding the index of the smallest number in the rotated array (verify with 
    example in the Problem Statement). A given number will be the "smallest" number in the rotated array if it is smaller
    than the number preceding it. 
    
    Thus, step through the array until that condition is achieved.

Binary Search Solution Explanation:
    Compare the middle element with the last element. If the middle element is smaller than the last element, repeat search
    on the left side of the middle element. If the middle element is greater than the last element, repeat search on the 
    right side of the middle element. 
    
    Smallest element is found when the current middle number is smallest than its succeeding number and preceeding number.
    
    E.g.:   [6, 7, 1, 2, 3, 4, 5]       mid=2 < last=5 -> repeat search on left side
            [6, 7, 1, 2]                mid=7 > last=2 -> repeat search on right side
            [7, 1, 2]                   mid=1 < last=2 and mid=1 < first=7 -> smallest number found
            1 is smallest number, thus: rotations = position = 2

'''

# Linear Search Solution:

def count_rotations_linear(array):
    pos = 1

    while pos < len(array):     # loops through the array linearly
        if pos > 0 and array[pos] < array[pos-1]:       # condition for smallest number
            return pos
        else:       # current number is not the smallest, increment position to next number
            pos += 1
    
    return 0        # return 0 not -1, since an array of length 1 or 0 has been rotated 0 times and not -1 times

# Binary Search Solution:

def count_rotations_binary(array):
    lo, hi = 0, len(array) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if mid > 0 and (array[mid] < array[mid-1] and array[mid] < array[mid+1]):       # condition for smallest number
            return mid
        elif array[mid] > array[hi]:        # condition for smallest number lying on the right
            lo = mid + 1
        elif array[mid] < array[hi]:        # condition for smallest number lying on the left
            hi = mid - 1
    
    return 0

# Testing Above Solutions:

input = [5, 6, 9, 0, 2, 3, 4]
output = count_rotations_binary(input)
expected = 3

print("Input: {}".format(input))
print("Output: {}".format(output))

if output != expected: print("~~~ FAIL - Output does not match Expected Output = {} ~~~".format(expected))
else: print("~~~ PASS - Output matches Expected Output = {} ~~~".format(expected))