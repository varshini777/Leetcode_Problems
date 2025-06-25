# 992. Subarrays with K Different Integers
# Solved
# Hard
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums and an integer k, return the number of good subarrays of nums.

# A good array is an array where the number of different integers in that array is exactly k.

# For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
# A subarray is a contiguous part of an array.

#  Example 1:

# Input: nums = [1,2,1,2,3], k = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]


#Naive Solution 
#Generating all the subarrays


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        c=0
        n=len(nums)
        
        for i in range(n):
            d=defaultdict(int)
            for j in range(i,n):
                d[nums[j]]+=1
                if len(d)==k:
                    c+=1
                elif len(d)>k:
                    break
        return c

        
#Two Pointer Approach 
from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmost(k):
            if k<0:
                return 0
            c=0
            n=len(nums)
            l=0
            r=0
            d=defaultdict(int)
            while(r<n):
                d[nums[r]]+=1
                while len(d)>k:
                    d[nums[l]]-=1
                    if d[nums[l]]==0:
                        del d[nums[l]]
                    l+=1
                c+=(r-l+1)
                r+=1
            return c 
                
        return atmost(k)-atmost(k-1)



# Time and Space Complexity:
# Time Complexity: O(n) – each element is processed at most twice (once added, once removed).
# Space Complexity: O(k) – the hash map stores counts for up to k distinct elements.

