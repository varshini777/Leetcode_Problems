# 76. Minimum Window Substring
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such 
# that every character in t (including duplicates) is included in the window. If there is no such substring,
# return the empty string "".

# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 
#Approach

from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = defaultdict(int)
        l = r = c = 0
        sIndex = -1
        minLen = float('inf')
        m = len(t)
        n = len(s)

        for ch in t:
            d[ch] += 1

        while r < n:
            if d[s[r]] > 0:
                c += 1
            d[s[r]] -= 1

            while c == m:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    sIndex = l

                d[s[l]] += 1
                if d[s[l]] > 0:
                    c -= 1
                l += 1

            r += 1

        return "" if sIndex == -1 else s[sIndex:sIndex + minLen]


#  Time and Space Complexity:
# Time Complexity: O(n + m) — where n is the length of s and m is the length of t.
# Space Complexity: O(m) — to store the frequency of characters in t.