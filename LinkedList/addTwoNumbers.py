#both the numbers are in reverse order, add them and print the result in reverse order
#both the linked lists could be of variable length

#Time complexity: O(max(m,n)) - m and n being length of linked lists. time taken for traversing this linked lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        curr = dummy
        carry =0
        while l1!= None or l2!=None or carry !=0:
            if l1:
                l1value = l1.val
            else:
                l1value= 0
            
            if l2:
                l2value = l2.val
            else:
                l2value=0
            
            colSum = l1value + l2value + carry

            #carry is generally taking the quotient in this case
            carry = colSum //10

            #remainder will be our new node
            
            new = ListNode(colSum %10)
            curr.next = new
            curr= new
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
