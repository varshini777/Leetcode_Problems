# 204. Count Primes
# Given an integer n, return the number of prime numbers that are strictly less than n.
# Example 1:
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Example 2:

# Input: n = 0
# Output: 0
# Example 3:

# Input: n = 1
# Output: 0
 

class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        p=[1]*n
        p[0]=0
        p[1]=0
        i=2
        while(i*i<=n):
            if(p[i]==1):
                for j in range(i*i,n,i):
                    p[j]=0
            i+=1
        return sum(p)
    
# Time Complexity: O(n log log n)
# Space Complexity: O(n)