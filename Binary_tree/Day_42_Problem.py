# 100. Same Tree
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
# Example 1:
#  Input: p = [1,2,3], q = [1,2,3]
# Output: true
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if(p==None or q==None):
            return p==q
        return (p.val==q.val) and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        
# Time Complexity: O(n) – where n is the number of nodes in the smaller tree
# Space Complexity: O(h) – h = height of the tree (due to recursion stack)