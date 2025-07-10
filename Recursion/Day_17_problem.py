# Description
# 22. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]

#Approach

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]
        def backtrack(openN,closeN):
            if openN==closeN==n:
                res.append("".join(stack))
                return
            if openN<n:
                stack.append('(')
                backtrack(openN+1,closeN)
                stack.pop()
            if closeN<openN:
                stack.append(')')
                backtrack(openN,closeN+1)
                stack.pop()
        backtrack(0,0)
        return res
    
# Time Complexity: O(2ⁿ) in worst case, but pruned
# Space Complexity: O(n) for recursion + stack

