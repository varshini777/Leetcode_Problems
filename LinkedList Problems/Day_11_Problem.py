# 237. Delete Node in a Linked List
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# There is a singly-linked list head and we want to delete a node node in it.

# You are given the node to be deleted node. You will not be given access to the first node of head.

# All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.

# Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

# The value of the given node should not exist in the linked list.
# The number of nodes in the linked list should decrease by one.
# All the values before node should be in the same order.
# All the values after node should be in the same order.

# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

#Approach
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        node.val=node.next.val
        node.next=node.next.next
        
        

# Time Complexity: O(1) — constant time operation
# Space Complexity: O(1) — no extra space used

        