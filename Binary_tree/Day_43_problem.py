# 199. Binary Tree Right Side View
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
# Example 1:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightview(self,root,level,st):
        if not root:
            return
        if level==len(st):
            st.append(root.val) 
        self.rightview(root.right,level+1,st)
        self.rightview(root.left,level+1,st)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        st=[]
        self.rightview(root,0,st)
        return st
        
# Time Complexity: O(n) – visit each node once
# Space Complexity: O(h) – recursion stack (h = tree height)