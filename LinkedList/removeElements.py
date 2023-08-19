#https://leetcode.com/problems/remove-linked-list-elements/description/
#remove elements from linked list that are eual to certain value

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        if head is None:
            return head
        dummy = ListNode(-1)
        dummy.next = head
    #print(curr)
        curr = dummy
        while curr.next is not None:
            if curr.next.val == val:
                curr.next = curr.next.next
                #curr=curr.next
            else:
                curr = curr.next
        #print(curr)
        #print dummy.next because dummy is pointing to -1 node
        return dummy.next

