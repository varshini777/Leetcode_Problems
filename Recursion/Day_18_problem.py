# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.

#Approach(Recursion)

class Solution:
    def solve(self,i,s,f,ans):
        if i==len(s):
            ans.append(f[:])
            return 
        self.solve(i+1,s,f+[s[i]],ans)
        self.solve(i+1,s,f,ans)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        f=[]
        ans=[]
        self.solve(0,nums,f,ans)
        return ans
#  Time Complexity: O(2ⁿ * n)
#  2ⁿ subsets, and each copy takes up to n time
#  Space Complexity: O(2ⁿ * n) for storing all subsets + O(n) recursion stack

#Bit Manpulation
class Solution:
    ans=[]
    n=len(nums)
    for i in range(0,1<<n):
        sub=[]
        for j in range(n):
            if(i & (1<<j)):
                sub.append(nums[j])
        ans.append(sub)
    return ans