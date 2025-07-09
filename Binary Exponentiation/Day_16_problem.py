# 50. Pow(x, n)
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
# Example 1:

# Input: x = 2.00000, n = 10
# Output: 1024.00000
# Example 2:

# Input: x = 2.10000, n = 3
# Output: 9.26100
# Example 3:

# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25

#Approach
class Solution:
    def myPow(self, x: float, n: int) -> float:
        nn=n
        ans=1.0
        if(nn<0):
            nn=-1*nn
        while(nn>0):
            if(nn%2==1):
                ans=ans*x
                nn=nn-1
            else:
                x=x*x
                nn=nn//2
        if(n<0):
            ans=float(1)/float(ans)
        return ans


#  Time Complexity: O(log n)
# Space Complexity: O(1)