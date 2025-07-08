# Reverse a Doubly Linked List
# Given a doubly linked list. Your task is to reverse the doubly linked list and return its head.
# Input: LinkedList: 3 <-> 4 <-> 5
# Output: 5 <-> 4 <-> 3

# Expected Time Complexity: O(n).
# Expected Auxiliary Space: O(1).

# Constraints:
# 1 <= number of nodes <= 106
# 0 <= node->data <= 104

#Approach
'''
class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def reverseDLL(self, head):
        if(head is None or head.next is None):
            return head
        
        curr=head
        while(curr):
            prev=curr.prev
            curr.prev=curr.next
            curr.next=prev
            if curr.prev is None:
                return curr
            curr=curr.prev
        
        
            
# Time Complexity: O(n) — each node is visited once
# Space Complexity: O(1) — no extra data structures used