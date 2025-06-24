# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
# A subarray is a contiguous part of the array.
# Example 1:

# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(goal):
            if goal<0:
                return 0
            l = 0
            r = 0
            c = 0
            s = 0
            n = len(nums)
            while r < n:
                s += nums[r]
                while s > goal:
                    s -= nums[l]
                    l += 1
                c += (r - l + 1)
                r += 1
            return c

        return atMost(goal) - atMost(goal - 1)


# Time and Space Complexity:
# Time Complexity: O(n), because each element is visited at most twice.
# Space Complexity: O(1), since only a few variables track the window and sums.