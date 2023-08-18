#https://leetcode.com/problems/linked-list-cycle/description/
#can be solved using hashmap as well
#with cycle approoach O(n) because we have to traverse atleast once
#LINKEDLIST CYCLE 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #sol using floyd's cycle finding algorithm
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        slow = head
        fast = head.next
        while slow !=fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next

        
        return True


            
