# 234. Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
#  Example 1:
# Input: head = [1,2,2,1]
# Output: true

#Approach

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_linkedlist(self,head):
        if head is None or head.next is None:
            return head
        new_head=self.reverse_linkedlist(head.next)
        front=head.next
        front.next=head
        head.next=None
        return new_head
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
        slow=head
        fast=head
        while fast.next is not None and fast.next.next is not None:
            slow=slow.next
            fast=fast.next.next
        new_head=self.reverse_linkedlist(slow.next)
        first=head
        second=new_head
        while second is not None:
            if first.val!=second.val:
                self.reverse_linkedlist(new_head)
                return False
            first=first.next
            second=second.next
        self.reverse_linkedlist(new_head)
        return True

# Time Complexity: O(n)
# Space Complexity: O(1)