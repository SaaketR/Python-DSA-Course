'''
Lesson 4 - Recursion and Dynamic Programming

Question:
    Write a function to find the length of the longest common subsequence between two sequences. 
    E.g.: The longest common subsequence of "serendipituous" and "precipitation" is "reipito" and its length is 7.

Test Cases:
    1. Input = "serendipitous", "precipitation" ; Output = 7
    2. Input = [1, 3, 5, 6, 7, 2, 5, 2, 3], [6, 2, 4, 7, 1, 5, 6, 2, 3] ; Output = 5
    3. Input = "longest", "stone" ; Output = 3
    4. Input = "asdfwevad", "opkpoiklklj" ; Output = 0
    5. Input = "dense", "condensed" ; Output = 5
    6. Input = " ", "opkpoiklklj" ; Output = 0
    7. Input = " ", " " ; Output = 0
    8. Input = "abcde", "badcfe" ; Output = 3

0-1 Knapsack Problem:
    Given n elements, each of which has a weight and a value, determine the maximum values that can be obtained by 
    selecting a subset of the elements weighing no more than total_weight.

'''

# Recursive Solution to Longest Common Subsequence problem [Time = O(2^N) ; Space = O(N)]
def lcs_recursive(seq1, seq2, idx1=0, idx2=0):
    if (len(seq1)==idx1 or len(seq2)==idx2):        # reached the end of either arrays
        return 0
    
    if (seq1[idx1] == seq2[idx2]):      # match found, add one to the length of the LCS
        return 1 + lcs_recursive(seq1, seq2, idx1+1, idx2+1)        # increment to the next element for both arrays
    else:
        return max(lcs_recursive(seq1, seq2, idx1+1, idx2), lcs_recursive(seq1, seq2, idx1, idx2+1))        # split and find the maximum length of commonality

# Recursive Solution to LCS w/ Memoization [Time = O(N*M) ; Space = O(N*M)]
def lcs_memoization(seq1, seq2):
    memo = {}       # maintaining a dictionary to store index pairs and whether the elements at the pairs match

    def recurse(idx1, idx2):
        key = idx1, idx2

        if key in memo:
            return memo[key]        # index was already checked, so no need to check again; return the value at the key
        
        if (idx1 == len(seq1) or idx2 == len(seq2)):        # reached the end of either arrays
            memo[key] = 0
        elif (seq1[idx1] == seq2[idx2]):        # match found, increment length of LCS
            memo[key] = 1 + recurse(idx1+1, idx2+1)
        else:
            memo[key] = max(recurse(idx1+1, idx2), recurse(idx1, idx2+1))       # containue search for commonality
        
        return memo[key]
    
    return recurse(0,0)     # start searching from the beginning of the arrays

# Dynamic Programming Solution to LCS []
def lcs_dp(seq1, seq2):
    n, m = len(seq1), len(seq2)
    results = [[0 for i in range(n+1)] for j in range(m+1)]     # creating a table of size (m+1) * (n+1) ; 0th row and column stores value of 0

    idx1 = 0
    while (idx1 < n):
        idx2 = 0
        while (idx2 < m):
            if (seq1[idx1] == seq2[idx2]):      # match found; diagonal element stores the incremented value at the current index pair
                results[idx1+1][idx2+1] = 1 + results[idx1][idx2]
            else:
                results[idx1+1][idx2+1] = max(results[idx1+1][idx2], results[idx1][idx2+1])
            idx2 += 1
        idx1 += 1
    
    return results[-1][-1]      # return the value at the last index pair in the table

# 0-1 Knapsack Problem Solution w/ DP
def knapsack_dp(total_weight, weights, values):
    n = len(weights)
    results = [[0 for i in range(total_weight+1)] for j in range(n+1)]

    idx = 0
    while (idx < n):
        tot = 0
        while (tot < total_weight+1):
            if (weights[idx] > tot):
                results[idx+1][tot] = results[idx][tot]
            else:
                results[idx+1][tot] = max(results[idx][tot], values[idx] + results[idx][tot - weights[idx]])
            tot += 1
        idx += 1
    
    return results[-1][-1]
