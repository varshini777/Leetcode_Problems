# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Example 1:
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

# Example 2:
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inMap = {val: idx for idx, val in enumerate(inorder)}
        return self._buildTree(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, inMap)

    def _buildTree(self, preorder, preStart, preEnd, inorder, inStart, inEnd, inMap):
        if preStart > preEnd or inStart > inEnd:
            return None

        root = TreeNode(preorder[preStart])
        inroot = inMap[root.val]
        numsleft = inroot - inStart

        root.left = self._buildTree(preorder, preStart + 1, preStart + numsleft,
                                    inorder, inStart, inroot - 1, inMap)
        root.right = self._buildTree(preorder, preStart + numsleft + 1, preEnd,
                                     inorder, inroot + 1, inEnd, inMap)

        return root

        
#  Time Complexity: O(n) – each node is processed once
#  Space Complexity: O(n) – for hashmap and recursion stack