#https://leetcode.com/problems/linked-list-cycle-ii/editorial/
#LINKEDLIST CYCLE 2 

#time: O(n) 
#space O(1) 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Using the floyd's hare and tortoise algorithm
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        
        if not fast or not fast.next:
            return None 
        
        #START OF SECOND ROUND bcz fast and slow ran into each other in 1st one
        #resetting the fast pointer
        fast = head
        #second round we just increment the fast pointer by 1 onli
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return fast
