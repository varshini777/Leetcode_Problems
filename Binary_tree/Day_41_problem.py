# 543. Diameter of Binary Tree
# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them
# Example 1:
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter=0
        self.dfsHeight(root)
        return self.diameter
    def dfsHeight(self,root):
        if not root:
            return 0
        lh=self.dfsHeight(root.left)
        rh=self.dfsHeight(root.right)
        self.diameter=max(self.diameter,lh+rh)
        return 1+max(lh,rh)
        
#  Time Complexity: O(n) – each node is visited once
#  Space Complexity: O(h) – recursion stack space (h = tree height)