# 678. Valid Parenthesis String
# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
# The following rules define a valid string:
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 
# Example 1:
# Input: s = "()"
# Output: true
# Example 2:
# Input: s = "(*)"
# Output: true

#Appraoch
class Solution:
    def checkValidString(self, s: str) -> bool:
        open_stack=[]
        star_stack=[]
        for i,char in enumerate(s):
            if char=='(':
                open_stack.append(i)
            elif char=='*':
                star_stack.append(i)
            elif char==')':
                if open_stack:
                    open_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        while open_stack and star_stack:
            if open_stack[-1]<star_stack[-1]:
                open_stack.pop()
                star_stack.pop()
            else:
                return False
        return not open_stack
    
# Time Complexity: O(n) — single pass + matching
# Space Complexity: O(n) — stacks for indices