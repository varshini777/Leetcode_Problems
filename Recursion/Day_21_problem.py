# 131. Palindrome Partitioning
# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:

# Input: s = "a"
# Output: [["a"]]

#Appraoch 

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        path=[]
        def findpartition(index):
            if index==len(s):
                res.append(path[:])
            for i in range(index,len(s)):
                if ispalindrome(s,index,i):
                    path.append(s[index:i+1])
                    findpartition(i+1)
                    path.pop()
        def ispalindrome(s,start,end):
            while start<end:
                if s[start]!=s[end]:
                    return False
                start+=1
                end-=1
            return True
        findpartition(0)
        return res
        
# Time Complexity: Exponential in the worst case (since we explore all partitions)
# Space Complexity: O(k * n) where k is number of partitions and n is max partition size

 