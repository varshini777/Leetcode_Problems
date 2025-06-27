# Lower Bound
# Given a sorted array of nums and an integer x, write a program to find the lower bound of x. The lower bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than or equal to a given key i.e. x.

# If no such index is found, return the size of the array.

# Examples:
# Input : nums= [1,2,2,3], x = 2

# Output:1

# Explanation: Index 1 is the smallest index such that arr[1] >= x.

# Input : nums= [3,5,8,15,19], x = 9

# Output: 3

# Explanation: Index 3 is the smallest index such that arr[3] >= x.

class Solution:
    def lowerBound(self, nums, x):
        low=0
        high=len(nums)-1
        ans=0
        while(low<=high):
            mid=(low+high)//2
            if(nums[mid]>=x):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    

# Time and Space Complexity:

# Time: O(log n) – binary search on a sorted array

# Space: O(1) – no extra space used