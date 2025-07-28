# Given an infinite supply of each denomination of Indian currency { 1, 2, 5, 10, 20, 50, 100, 200, 500, 2000 } and a target value N.
# Find the minimum number of coins and/or notes needed to make the change for Rs N. You must return the list containing the value of coins required. 
# Example 1:

# Input: N = 43
# Output: 20 20 2 1
# Explaination: 
# Minimum number of coins and notes needed 
# to make 43. 

class Solution:
    def minPartition(self, N):
        k=[1, 2, 5, 10, 20, 50, 100, 200, 500, 2000 ]
        h=len(k)-1
        l=[]
        while N>0:
            if(k[h]<=N):
                N=N-k[h]
                l.append(k[h])
            else:
                h=h-1
        return l
    
# Time Complexity: O(1) – max 10 denominations
# Space Complexity: O(1) – output list size is limited by amount