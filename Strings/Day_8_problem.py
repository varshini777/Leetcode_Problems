# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

#Approach
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=0
        h=len(strs)-1
        strs.sort()
        s=""
        if len(strs)=="":
            return ""
        if len(strs)==1:
            return strs[0]
        first=strs[l]
        last=strs[h]
        
        for i in range(min(len(first),len(last))):
            if(first[i]==last[i]):
                s+=first[i]
            else:
                break 
        
        return s

# Time Complexity: O(n log n + m), where n is the number of strings (due to sorting) and m is the length of the common prefix.
#  Space Complexity: O(1) — constant extra space beyond the output string.


            
            

        