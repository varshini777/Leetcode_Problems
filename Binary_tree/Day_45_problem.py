# 101. Symmetric Tree
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetricUtil(self,root1,root2):
        if root1 is None or root2 is None:
            return root1==root2
        return (root1.val==root2.val and self.isSymmetricUtil(root1.left,root2.right) and self.isSymmetricUtil(root1.right,root2.left))

        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.isSymmetricUtil(root.left,root.right)
        
#  Time Complexity: O(n) – every node is visited once
#  Space Complexity: O(h) – due to recursion stack (h = tree height)