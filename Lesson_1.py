'''
Lesson 1 - Binary Search, Linked Lists, and Complexities

Question 1:
    Alice has some array with numbers written on them. She arranges the cards in decreasing order, and lays them out face down
    in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards
    as possible. Write a function to help Bob locate the card.

Test Cases:
1. {'array': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}
2. {'array': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}
3. {'array': [4, 2, 1, -1], 'query': 4}
4. {'array': [3, -1, -9, -127], 'query': -127}
5. {'array': [6], 'query': 6}
6. {'array': [9, 7, 5, 2, -9], 'query': 4}
7. {'array': [], 'query': 7}
8. {'array': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3}
9. {'array': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 6}

'''

# Linear Search Solution [Time = O(N); Space = O(1)]

def linear_search(array, query):
    position = 0

    while position < len(array):
        if array[position] == query:
            return position
        position += 1

    return -1

# Binary Search Solution [Time = O(log(N)); Space = O(1)]

def binary_search_general(array, query):      # General binary search algorithm
    lo, hi = 0, len(array)-1
    
    while lo <= hi:
        mid = (lo+hi)//2
        mid_num = array[mid]
        if mid_num == query:
            return mid
        elif mid_num < query:
            hi = mid - 1
        elif mid_num > query:
            lo = mid + 1
    
    return -1

def binary_search_first(array, query):      # Recursive use of binary search to find the first known occurance of the query
    
