# You are given a string S of size N that represents the prefix form of a valid mathematical expression. The string S contains only lowercase and uppercase alphabets as operands and the operators are +, -, *, /, %, and ^.Convert it to its infix form.

# Example 1:

# Input: 
# *-A/BC-/AKL
# Output: 
# ((A-(B/C))*((A/K)-L))
# Explanation: 
# The above output is its valid infix form.

class Solution:
    def is_operator(self,c):
        return c in "`+-*/^"
    def preToInfix(self, pre_exp):
        st=[]
        # Code here
        for i in reversed(pre_exp):
            if self.is_operator(i):
                op1=st.pop()
                op2=st.pop()
                new_exp=f"({op1}{i}{op2})"
                st.append(new_exp)
            else:
                st.append(i)
        return st[0]
    
# Time Complexity: O(n)
# Space Complexity: O(n)