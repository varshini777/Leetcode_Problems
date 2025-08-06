# Bottom View of Binary Tree
# Given a binary tree, return an array where elements represent the bottom view of the binary tree from left to right.

# Note: If there are multiple bottom-most nodes for a horizontal distance from the root, then the later one in the level order traversal is considered. For example, in the below diagram, 7 and 34 both are the bottommost nodes at a horizontal distance of 0 from the root, here 34 will be considered.

# Input: root[] = [1, 3, 2]
# Output: [3 1 2]

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
from queue import Queue
class Solution:
    def bottomView(self, root):
        ans=[]
        if root is None:
            return ans
        d=defaultdict(int)
        q=Queue()
        q.put((root,0))
        while not q.empty():
            it=q.get()
            node,line=it[0],it[1]
            d[line]=node.data
            if node.left:
                q.put((node.left,line-1))
            if node.right:
                q.put((node.right,line+1))
        for k,v in sorted(d.items()):
            ans.append(v)
        return ans
        
#    Time Complexity: O(n) – each node is visited once
#    Space Complexity: O(n) – for the queue and the map