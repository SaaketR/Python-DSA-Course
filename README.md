# Python-DSA-Course
Data Structures and Algorithms Course from Jovian.ai

Websites and resources referenced:
    1. Jovian.ai
    2. GeeksForGeeks.org

Terminology and Definitions:

    1. Algorithms
        -> A list of statements that can be converted into code and executed by a computer on different sets of inputs.

    2. Complexity
        -> Measures the amount of time and/or space required by tan algorithm for an output of a given size N. Refers to worst-case complexity.
    
    3. Time Complexity
        -> Depends on the number of operations performed in each iteration and the time taken to execute the statements.
    
    4. Space Complexity
        -> Total memory used by an algorithm/program, including the space for input values for execution
    
    5. Big O Notation
        -> Worst-case complexity is expressed using Big O notation - O(N), O(log(N)), etc.

    6. Sorted Array
        -> A array where all elements are arranged in ascending order (E.g.: [1, 2, 3, 4])
    
    7. Rotating Arrays
        -> The process of removing the last element of a sorted array and adding it before the first element of the array.
        (E.g.: [0, 1, 2, 3, 4] yields [4, 3, 0, 1, 2] when rotated 2 times)

    8. Binary Search Trees
        -> Binary tree where the left subtree contains nodes with keys lexicographically smaller than the node's key and the right subtree contains nodes with keys lexicographically greater than the node's key.
    
    9. Balanced Tree
        -> A binary tree is said to be balanced if the left and right subtree of any node shouldn't differ in height or depth by more than 1.

Covered Algorithms:

    1. Linear Search
        -> Searching through a list in a linear fashion (element after element)
            i. Create a varible with 'position' 0
            ii. Check if number at index 'position' is equal to query 
            iii. If number matches, return 'position' as the answer to the question
            iv. If not, increment 'position' and repeat steps until we reach the end of the array
            v. If numer was not found, return -1
        -> Time Complexity = O(N)
        -> Space Complexity = O(1)
    
    2. Binary Search
        -> Pick random position, determine to which side of the random position is the query located.
            i. Find the middle element of the list
            ii. If this matches the query, return the middle element
            iii. If the query is less than the middle element, repeat the search with first half of the list
            iv. If the query is more than the middle element, repeat the search with second half of the list
            v. If no more elements, return -1
        -> Time Complexity = O(log(N))
        -> Space Complexity = O(1)
    
    3. Inorder Traversal
        -> Traverse the left subtree, visit the root, then traverse the right subtree.
            -> node.left + [node.key] + node.right
        -> Returns nodes of BSTs in non-decreasing order
    
    4. Preorder Traversal
        -> Visit the root, traverse the left subtree, then traverse the right subtree.
            -> [node.key] + node.left + node.right
        -> Used to create a copy of the tree and also used to get the prefix expressions of an expression tree.
    
    5. Postoder Traversal
        -> Traverse the left subtree, traverse the right subtree, then visit the root
            -> node.left + node.right + [node.key]
        -> Used to delete the tree and also used to get the postfix expressions of an expression tree.
    