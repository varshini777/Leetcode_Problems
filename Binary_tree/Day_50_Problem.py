# 106. Construct Binary Tree from Inorder and Postorder Traversal
# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

# Example 1:
# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: inorder = [-1], postorder = [-1]
# Output: [-1]
 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder)!=len(postorder):
            return None
        inMap={val:idx for idx,val in enumerate(inorder)}
        return self._buildTree(inorder,0,len(inorder)-1,postorder,0,len(postorder)-1,inMap)
    def _buildTree(self,inorder,instart,inend,postorder,poststart,postend,inMap):
        if poststart>postend or instart>inend:
            return None
        
        root=TreeNode(postorder[postend])
        inroot=inMap[postorder[postend]]
        numsleft=inroot-instart
        root.left=self._buildTree(inorder,instart,inroot-1,postorder,poststart,poststart+numsleft-1,inMap)
        root.right=self._buildTree(inorder,inroot+1,inend,postorder,poststart+numsleft,postend-1,inMap)
        return root

# Time Complexity: O(n) — each node is processed once.
# Space Complexity: O(n) — for hashmap + recursion stack.     