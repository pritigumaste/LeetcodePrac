#https://leetcode.com/problems/reverse-linked-list/editorial/
#Linkedist reversal in ITERATIVE WAY 
#time O(n) - because of time needed for linkedlist traversal
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            nextTemp = current.next
            current.next = prev
            prev = current
            current = nextTemp
        return prev
