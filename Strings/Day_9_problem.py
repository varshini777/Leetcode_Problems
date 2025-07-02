# 1781. Sum of Beauty of All Substrings

# The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

# For example, the beauty of "abaacc" is 3 - 1 = 2.
# Given a string s, return the sum of beauty of all of its substrings.
# Example 1:

# Input: s = "aabcb"
# Output: 5
# Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
# Example 2:

# Input: s = "aabcbaa"
# Output: 17

#Approach
class Solution:
    def beautySum(self, s: str) -> int:
        total=0
        n=len(s)
        for i in range(n):
            freq=[0]*26
            for j in range(i,n):
                idx=ord(s[j])-ord('a')
                freq[idx]+=1
                max_freq=max(freq)
                min_freq=min(i for i in freq if i>0)
                total+=max_freq-min_freq
        return total
    
#  Time Complexity: O(n² * 26) — for each substring, we check up to 26 character frequencies.
# Space Complexity: O(26) — for the frequency array.