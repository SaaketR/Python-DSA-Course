# Python-DSA-Course
Data Structures and Algorithms Course from Jovian.ai

Terminology and Definitions:

    1. Algorithms
        -> A list of statements that can be converted into code and executed by a computer on different sets of inputs.

    2. Complexity
        -> Measures the amount of time and/or space required by tan algorithm for an output of a given size N. Refers to 
        worst-case complexity.
    
    3. Time Complexity
        -> Depends on the number of operations performed in each iteration and the time taken to execute the statements.
    
    4. Space Complexity
        -> Total memory used by an algorithm/program, including the space for input values for execution
    
    5. Big O Notation
        -> Worst-case complexity is expressed using Big O notation - O(N), O(log(N)), etc.


Covered Algorithms:

    1. Linear Search
        -> Searching through a list in a linear fashion (element after element)
            i. Create a varible with 'position' 0
            ii. Check if number at idex 'position' is equal to query 
            iii. If number matches, return 'position' as the answer to the question
            iv. If not, increment 'position' and repeat steps until we reach the end of the array
            v. If numer was not found, return -1
        -> Time Complexity = O(N)
        -> Space Complexity = O(1)
    
    2. Binary Search
        -> Pick random position, determine to which side of the random position is the query located.
            i. Find the middle element of the list
            ii. If this matches the query, return the middle element
            iii. If the query is less than the middle element, search the first half of the list
            iv. If the query is more than the middle element, search the second half of the list
            v. If no more elements, return -1
        -> Time Complexity = O(log(N))
        -> Space Complexity = O(1)
    