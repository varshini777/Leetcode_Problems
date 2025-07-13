# 90. Subsets II
# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:
# Input: nums = [0]
# Output: [[],[0]]

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        ds=[]
        def findsubsets(ind):
            ans.append(ds[:])
            for i in range(ind,len(nums)):
                if i!=ind and nums[i]==nums[i-1]:
                    continue
                ds.append(nums[i])
                findsubsets(i+1)
                ds.pop()

        nums.sort()
        findsubsets(0)
        return ans

# Time Complexity: O(2ⁿ) (but less due to skipping duplicates)
# Space Complexity: O(n) recursion + O(2ⁿ) output size