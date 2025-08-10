# 662. Maximum Width of Binary Tree
# Given the root of a binary tree, return the maximum width of the given tree.

# The maximum width of a tree is the maximum width among all levels.

# The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

# It is guaranteed that the answer will in the range of a 32-bit signed integer.

# Example 1:
# Input: root = [1,3,2,5,3,null,9]
# Output: 4
# Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = 0
        q = deque([(root, 0)])  # node, index

        while q:
            size = len(q)
            _, first_idx = q[0]
            for _ in range(size):
                node, idx = q.popleft()
                idx -= first_idx  # normalize to avoid overflow
                if node.left:
                    q.append((node.left, idx * 2 + 1))
                if node.right:
                    q.append((node.right, idx * 2 + 2))
         
            ans = max(ans, idx + 1)

        return ans

#  Time Complexity: O(n) – visiting all nodes once
#  Space Complexity: O(n) – queue for BFS