#https://leetcode.com/problems/remove-duplicates-from-sorted-list/  
#1-2-2-4 ->o/p should be 1-2-4
#Time complexity: O(n) because we have to traverse through the linkedlist atleast once

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        
        if head is None:
            return None
        while curr.next:
        #dont forget to aadd .val because we are comparing the values before proceeding ahead.
            if curr.val == curr.next.val:
                #print(curr)
                #print(curr.next)
                curr.next = curr.next.next
                 
            else:
                curr = curr.next
        return head


